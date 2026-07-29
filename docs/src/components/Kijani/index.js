import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';

import styles from './styles.module.css';
import BoardArt from './BoardArt';

export { BoardArt };

/* ------------------------------------------------------------------
   Kijani component library.

   Every visual pattern from the homepage, packaged for reuse on any
   page (and in MDX docs via src/theme/MDXComponents.js). All colours
   come from the --kj-* tokens in src/css/custom.css.

   import {
     Hero, SpecStrip, Section, SectionTitle, Refdes, Split,
     FeatureGrid, FeatureCard, Terminal, ConfigList, ConfigNote,
     CtaBand, Button, BoardArt,
   } from '@site/src/components/Kijani';
------------------------------------------------------------------- */

/**
 * Silkscreen-style reference-designator eyebrow.
 * <Refdes id="U1">Everything the robot needs is on the PCB</Refdes>
 */
export function Refdes({ id, children, className }) {
  return (
    <p className={clsx(styles.refdes, className)}>
      <span className={styles.refdesId}>{id}</span>
      {children}
    </p>
  );
}

/** Section heading in the display face. Renders an <h2> by default. */
export function SectionTitle({ as: Tag = 'h2', children, className }) {
  return <Tag className={clsx(styles.sectionTitle, className)}>{children}</Tag>;
}

/**
 * Link-button in the three homepage variants.
 * <Button to="/docs/intro" variant="primary">Build your bot</Button>
 * variant: 'primary' (copper) | 'ghost' (outline) | 'ghost-light' (gold outline, for dark bg)
 */
export function Button({ to, variant = 'primary', className, children, ...rest }) {
  const variants = {
    primary: styles.btnPrimary,
    ghost: styles.btnGhost,
    'ghost-light': styles.btnGhostLight,
  };
  return (
    <Link className={clsx(styles.btn, variants[variant], className)} to={to} {...rest}>
      {children}
    </Link>
  );
}

/**
 * Full-width band with the standard padding and palette.
 * Props: dark (ink background), refdes + eyebrow, title, className.
 * When `title`/`refdes` are given they render at container level; for
 * custom layouts (e.g. a Split with the title inside one column) omit
 * them and compose <Refdes>/<SectionTitle> in children instead.
 */
export function Section({ dark = false, refdes, eyebrow, title, className, children }) {
  return (
    <section className={clsx(styles.section, dark && styles.sectionDark, className)}>
      <div className="container">
        {refdes != null && <Refdes id={refdes}>{eyebrow}</Refdes>}
        {title != null && <SectionTitle>{title}</SectionTitle>}
        {children}
      </div>
    </section>
  );
}

/** Two equal columns (stacks below 996px). Used by the API section. */
export function Split({ className, children }) {
  return <div className={clsx(styles.split, className)}>{children}</div>;
}

/**
 * Page hero: copy on the left, optional art on the right, optional
 * strip (e.g. <SpecStrip/>) pinned to the bottom edge.
 * `title`, `lead`, `actions`, `art` all accept arbitrary nodes.
 */
export function Hero({ eyebrow, title, lead, actions, finePrint, art, strip, className }) {
  return (
    <header className={clsx(styles.hero, className)}>
      <div className={clsx('container', styles.heroInner)}>
        <div>
          {eyebrow != null && <p className={styles.heroEyebrow}>{eyebrow}</p>}
          <h1 className={styles.heroTitle}>{title}</h1>
          {lead != null && <p className={styles.heroLead}>{lead}</p>}
          {actions != null && <div className={styles.heroActions}>{actions}</div>}
          {finePrint != null && <p className={styles.heroFinePrint}>{finePrint}</p>}
        </div>
        {art != null && <div className={styles.heroArt}>{art}</div>}
      </div>
      {strip}
    </header>
  );
}

/**
 * Mono spec ticker.
 * <SpecStrip items={[{ value: '~R600', label: 'full kit' }, ...]} />
 */
export function SpecStrip({ items = [], className }) {
  return (
    <div className={clsx(styles.specStrip, className)}>
      <div className={clsx('container', styles.specStripInner)}>
        {items.map(({ value, label }) => (
          <span key={`${value}-${label}`}>
            <strong>{value}</strong> {label}
          </span>
        ))}
      </div>
    </div>
  );
}

/** One card: copper-edged, refdes tag, title, body. */
export function FeatureCard({ refdes, title, children, className }) {
  return (
    <article className={clsx(styles.featureCard, className)}>
      {refdes != null && <span className={styles.featureRef}>{refdes}</span>}
      <h3>{title}</h3>
      {children}
    </article>
  );
}

/**
 * Responsive 3/2/1-column card grid. Either pass `features`
 * ({ ref, title, body }[]) or compose <FeatureCard> children.
 */
export function FeatureGrid({ features, className, children }) {
  return (
    <div className={clsx(styles.featureGrid, className)}>
      {features
        ? features.map((f) => (
            <FeatureCard key={f.ref ?? f.title} refdes={f.ref} title={f.title}>
              {f.body}
            </FeatureCard>
          ))
        : children}
    </div>
  );
}

/**
 * Faux terminal for HTTP examples.
 * lines: array of { comment } | { get } | { text } | {} (blank line).
 * <Terminal host="10.10.10.10" lines={[
 *   { comment: '# full speed ahead' },
 *   { get: '/processcontrol?M1=255&M2=255' },
 *   {},
 *   { get: '/quickstatus' },
 * ]} />
 */
export function Terminal({ host, lines = [], ariaLabel = 'Example API requests', className, children }) {
  return (
    <div className={clsx(styles.terminal, className)} aria-label={ariaLabel}>
      <div className={styles.terminalBar}>
        <span />
        <span />
        <span />
        {host != null && <em>{host}</em>}
      </div>
      <pre className={styles.terminalBody}>
        <code>
          {lines.length > 0
            ? lines.map((line, i) => (
                // eslint-disable-next-line react/no-array-index-key
                <React.Fragment key={i}>
                  {line.comment != null && <span className={styles.tCmt}>{line.comment}</span>}
                  {line.get != null && (
                    <>
                      <span className={styles.tGet}>GET</span> {line.get}
                    </>
                  )}
                  {line.text != null && line.text}
                  {i < lines.length - 1 && '\n'}
                </React.Fragment>
              ))
            : children}
        </code>
      </pre>
    </div>
  );
}

/**
 * Chip list of robot configurations.
 * <ConfigList items={[{ name: 'Flipper', note: 'servo-actuated arm' }, ...]} />
 */
export function ConfigList({ items = [], className }) {
  return (
    <ul className={clsx(styles.configList, className)}>
      {items.map(({ name, note }) => (
        <li key={name}>
          <strong>{name}</strong>
          <span>{note}</span>
        </li>
      ))}
    </ul>
  );
}

/** Constrained-width note paragraph to follow a ConfigList. */
export function ConfigNote({ children, className }) {
  return <p className={clsx(styles.configNote, className)}>{children}</p>;
}

/**
 * Green gradient call-to-action band: title + copy left, stacked
 * actions right.
 * <CtaBand title="Want a bot?" actions={<><Button .../><Button .../></>}>
 *   <p>copy...</p>
 * </CtaBand>
 */
export function CtaBand({ title, children, actions, className }) {
  return (
    <section className={clsx(styles.section, styles.ctaSection, styles.onDark, className)}>
      <div className={clsx('container', styles.ctaInner)}>
        <div>
          {title != null && <SectionTitle>{title}</SectionTitle>}
          {children}
        </div>
        <div className={styles.ctaActions}>{actions}</div>
      </div>
    </section>
  );
}
