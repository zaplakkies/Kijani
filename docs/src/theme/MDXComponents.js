import MDXComponents from '@theme-original/MDXComponents';
import {
  Refdes,
  Terminal,
  Button as KjButton,
  FeatureGrid,
  FeatureCard,
  ConfigList,
  BoardArt,
} from '@site/src/components/Kijani';

/**
 * Makes the Kijani components available in every .md/.mdx doc page
 * without an import line, e.g.:
 *
 *   <Refdes id="TX">Drive it over HTTP</Refdes>
 *
 *   <Terminal host="10.10.10.10" lines={[
 *     { comment: '# battery + telemetry' },
 *     { get: '/quickstatus' },
 *   ]} />
 *
 * Button is exposed as KjButton to avoid clashing with anything else.
 */
export default {
  ...MDXComponents,
  Refdes,
  Terminal,
  KjButton,
  FeatureGrid,
  FeatureCard,
  ConfigList,
  BoardArt,
};
