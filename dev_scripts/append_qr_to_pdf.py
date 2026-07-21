# Reads ESP32 MAC address, generates a QR code based on that (see qr_gen.py)
# & appends it to a PDF file with an index above
# Usage: pio run -t qr_gen

# This file uses helpers from qr_gen.py

import tempfile
from pathlib import Path
import io
import datetime
import re

Import("env")
import qr_gen

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4, portrait
    from reportlab.lib.units import cm
    from reportlab.lib.utils import ImageReader
except Exception:
    canvas = None
    A4 = None
    cm = None
    ImageReader = None

try:
    from PyPDF2 import PdfReader, PdfWriter
except Exception:
    PdfReader = PdfWriter = None

OUT_DIR = Path("assets") / "qr"
OUT_DIR.mkdir(parents=True, exist_ok=True)

STICKER_W_CM = 1.51
STICKER_H_CM = 1.64
COLS = 6
ROWS = 8

def create_pdf_page(img_pil, out_pdf: Path, index=None, cell_index=0,
                    cols=COLS, rows=ROWS, margin_cm=0.5, spacing_cm=0.2):
    page_w, page_h = portrait(A4)
    c = canvas.Canvas(str(out_pdf), pagesize=(page_w, page_h))

    sticker_w = STICKER_W_CM * cm
    sticker_h = STICKER_H_CM * cm
    margin = margin_cm * cm
    spacing = spacing_cm * cm

    col = cell_index % cols
    row = cell_index // cols
    if row >= rows:
        # Should not happen; handled in append_action
        row = row % rows
        c.showPage()

    x_start = margin + col * (sticker_w + spacing)
    y_start = page_h - margin - sticker_h - row * (sticker_h + spacing)

    bio = io.BytesIO()
    img_pil.save(bio, format="PNG")
    bio.seek(0)
    img_reader = ImageReader(bio)

    c.drawImage(img_reader, x_start, y_start,
                width=sticker_w, height=sticker_h,
                preserveAspectRatio=True, mask='auto')

    if index is not None:
        c.setFont("Helvetica", 8)
        c.setFillColorRGB(0, 0, 0)
        c.drawCentredString(x_start + sticker_w/2,
                            y_start + sticker_h + (0.15*cm),
                            str(index))

    # Invisible timestamp (to avoid confusion with sticker numbers)
    c.setFont("Helvetica", 1)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(0.1, 0.1, datetime.datetime.now().isoformat())

    c.showPage()
    c.save()
    return out_pdf

def append_or_create_pdf(target_pdf: Path, new_pdf: Path):
    target_pdf.parent.mkdir(parents=True, exist_ok=True)
    if PdfReader is None or PdfWriter is None:
        new_pdf.replace(target_pdf)
        return target_pdf

    writer = PdfWriter()
    if target_pdf.exists():
        old = PdfReader(str(target_pdf))
        for p in old.pages:
            writer.add_page(p)
    new = PdfReader(str(new_pdf))
    for p in new.pages:
        writer.add_page(p)

    tmp = Path(tempfile.NamedTemporaryFile(suffix=".pdf", delete=False).name)
    with open(tmp, "wb") as fh:
        writer.write(fh)
    tmp.replace(target_pdf)
    return target_pdf

def append_action(target, source, env):
    img_obj, ssid = qr_gen.create_qr_for_attached_device(save_png=False)
    if img_obj is None:
        print("Failed to create image; SSID:", ssid)
        return 1

    desired_dpi = 300
    px_w = int(round((STICKER_W_CM / 2.54) * desired_dpi))
    px_h = int(round((STICKER_H_CM / 2.54) * desired_dpi))
    if img_obj.width < px_w or img_obj.height < px_h:
        img_obj = img_obj.resize((px_w, px_h), resample=2)

    target_pdf = OUT_DIR / "stickers.pdf"

    # Determine the next cell index by reading existing PDF labels
    if target_pdf.exists() and PdfReader is not None:
        reader = PdfReader(str(target_pdf))
        text_all = ''
        for page in reader.pages:
            try:
                txt = page.extract_text()
            except Exception:
                txt = ''
            if txt:
                text_all += txt
        # Remove the invisible timestamp strings (format YYYY-MM-DDThh:mm:ss.micro)
        text_clean = re.sub(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+', '', text_all)
        nums = re.findall(r'\d+', text_clean)
        if nums:
            total_qrs = max(map(int, nums))
        else:
            total_qrs = 0
        cell_index = total_qrs % (COLS * ROWS)
        next_index = total_qrs + 1
    else:
        cell_index = 0
        next_index = 1

    tmp_pdf = Path(tempfile.NamedTemporaryFile(suffix=".pdf", delete=False).name)
    try:
        create_pdf_page(
            img_obj, tmp_pdf,
            index=next_index,
            cell_index=cell_index
        )
    except Exception as e:
        print("Failed to create PDF page:", e)
        return 1

    try:
        # Merge or append the new sticker into the existing PDF
        if PdfReader is None or PdfWriter is None:
            # Fallback: just replace if PDF libs not available
            tmp_pdf.replace(target_pdf)
        elif target_pdf.exists():
            reader_target = PdfReader(str(target_pdf))
            if cell_index != 0:
                # Overlay new sticker onto last page
                reader_new = PdfReader(str(tmp_pdf))
                reader_target.pages[-1].merge_page(reader_new.pages[0])
                writer = PdfWriter()
                for p in reader_target.pages:
                    writer.add_page(p)
                tmp2 = Path(tempfile.NamedTemporaryFile(suffix=".pdf", delete=False).name)
                with open(tmp2, "wb") as fh:
                    writer.write(fh)
                tmp2.replace(target_pdf)
            else:
                # Last page was full; append as new page
                reader_new = PdfReader(str(tmp_pdf))
                writer = PdfWriter()
                for p in reader_target.pages:
                    writer.add_page(p)
                for p in reader_new.pages:
                    writer.add_page(p)
                tmp2 = Path(tempfile.NamedTemporaryFile(suffix=".pdf", delete=False).name)
                with open(tmp2, "wb") as fh:
                    writer.write(fh)
                tmp2.replace(target_pdf)
        else:
            # No existing PDF; just rename the temp PDF as target
            tmp_pdf.replace(target_pdf)

        print(f"Appended QR #{next_index} (cell {cell_index}) to {target_pdf}")
    except Exception as e:
        print("Failed to append PDF:", e)
        return 1

    print("Done. SSID:", ssid)
    return 0

env.AddCustomTarget(
    "append_qr_to_pdf",
    None,
    append_action,
    title="Append QR to stickers.pdf",
    description="Generate in-memory sticker QR (from attached device) and append to assets/qr/stickers.pdf"
)
