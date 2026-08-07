import React from 'react';
import styles from './styles.module.css';

/**
 * Stylised render of the Kijani PCB, drawn as inline SVG.
 * Colours come from the --kj-* tokens; the copper traces animate on load
 * (disabled under prefers-reduced-motion).
 */
export default function BoardArt({ className }) {
  return (
    <svg
      className={className ? `${styles.board} ${className}` : styles.board}
      viewBox="0 0 420 300"
      role="img"
      aria-label="Stylised diagram of the Kijani PCB: ESP32 module, dual motor drivers, servo headers, LiPo charger and USB port on one board"
    >
      {/* board substrate */}
      <rect x="8" y="8" width="404" height="284" rx="14" className={styles.boardBase} />
      <rect x="8" y="8" width="404" height="284" rx="14" className={styles.boardSheen} />

      <text x="210" y="30" className={styles.silk} textAnchor="middle">KIJANI</text>

      {/* mounting holes */}
      {[[26, 26], [394, 26], [26, 274], [394, 274]].map(([cx, cy]) => (
        <g key={`${cx}-${cy}`}>
          <circle cx={cx} cy={cy} r="8" className={styles.holeRing} />
          <circle cx={cx} cy={cy} r="4.5" className={styles.holeCore} />
        </g>
      ))}

      {/* copper traces (drawn on load) */}
      <g className={styles.traces}>
        <path d="M150 120 H96 V180 H60" />
        <path d="M150 138 H110 V206 H60" />
        <path d="M270 120 H324 V180 H360" />
        <path d="M270 138 H310 V206 H360" />
        <path d="M180 176 V216 H140 V252" />
        <path d="M204 176 V228" />
        <path d="M240 176 V216 H280 V252" />
        <path d="M210 92 V64 H120 V44" />
        <path d="M228 92 V58 H300 V44" />
      </g>

      {/* trace pads */}
      <g className={styles.pads}>
        {[[60, 180], [60, 206], [360, 180], [360, 206], [140, 252], [204, 228], [280, 252], [120, 44], [300, 44]].map(
          ([cx, cy]) => <circle key={`${cx}-${cy}`} cx={cx} cy={cy} r="5" />,
        )}
      </g>

      {/* ESP32 module */}
      <g>
        <rect x="150" y="92" width="120" height="84" rx="4" className={styles.chip} />
        <rect x="150" y="92" width="120" height="26" rx="4" className={styles.chipShield} />
        <text x="210" y="150" className={styles.chipLabel} textAnchor="middle">ESP32</text>
        <text x="210" y="109" className={styles.chipPin} textAnchor="middle">U1</text>
      </g>

      {/* motor drivers */}
      <g>
        <rect x="34" y="168" width="54" height="50" rx="4" className={styles.chipSmall} />
        <text x="61" y="197" className={styles.chipPinSmall} textAnchor="middle">M1</text>
        <rect x="332" y="168" width="54" height="50" rx="4" className={styles.chipSmall} />
        <text x="359" y="197" className={styles.chipPinSmall} textAnchor="middle">M2</text>
      </g>

      {/* servo headers */}
      <g>
        <rect x="122" y="248" width="36" height="20" rx="3" className={styles.header} />
        <text x="140" y="262" className={styles.headerLabel} textAnchor="middle">S1</text>
        <rect x="262" y="248" width="36" height="20" rx="3" className={styles.header} />
        <text x="280" y="262" className={styles.headerLabel} textAnchor="middle">S2</text>
      </g>

      {/* USB + charger */}
      <rect x="100" y="26" width="40" height="18" rx="3" className={styles.header} />
      <text x="120" y="39" className={styles.headerLabel} textAnchor="middle">USB</text>
      <rect x="280" y="26" width="40" height="18" rx="3" className={styles.header} />
      <text x="300" y="39" className={styles.headerLabel} textAnchor="middle">CHG</text>

      {/* silkscreen */}
      <text x="210" y="284" className={styles.silkSmall} textAnchor="middle">AP 10.10.10.10</text>
    </svg>
  );
}
