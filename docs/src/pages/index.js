import React from 'react';
import Layout from '@theme/Layout';
import { GithubLogoIcon } from '@phosphor-icons/react';

import {
  BoardArt,
  Button,
  ConfigList,
  ConfigNote,
  CtaBand,
  FeatureGrid,
  Hero,
  Refdes,
  Section,
  SectionTitle,
  SpecStrip,
  Split,
  Terminal,
} from '@site/src/components/Kijani';

/* ------------------------- page content ------------------------- */

const SPECS = [
  { value: '~R600', label: 'full kit' },
  { value: '1S LiPo', label: 'or 18650' },
  { value: 'N20', label: 'gear motors' },
  { value: 'http://10.10.10.10', label: 'to drive' },
];

const FEATURES = [
  {
    ref: 'M1·M2',
    title: 'Dual motor drivers',
    body: 'Two DC motor outputs on board — enough for a differential drive base or a drive-plus-weapon setup, no external driver modules.',
  },
  {
    ref: 'S1·S2',
    title: 'Two servo outputs',
    body: 'Drive a flipper arm, a steering linkage or a weapon actuator directly. Boost regulator available when servos need more voltage.',
  },
  {
    ref: 'CHG',
    title: 'LiPo charging built in',
    body: 'Single-cell charging on the board itself. Plug in over USB, charge the battery, unplug and fight.',
  },
  {
    ref: 'AP',
    title: 'WiFi access point',
    body: 'The board hosts its own network. Connect any phone or laptop, open the browser — no app, no pairing, no transmitter.',
  },
  {
    ref: 'FS',
    title: 'Your UI, hosted on the bot',
    body: 'Control pages are plain HTML, CSS and JavaScript stored in LittleFS on the ESP32. Upload your own and the robot serves it.',
  },
  {
    ref: 'API',
    title: 'Open HTTP API',
    body: 'Motors, servos, telemetry, settings and files are all plain HTTP endpoints. Anything that can make a request can drive the bot.',
  },
];

const API_LINES = [
  { comment: '# full speed ahead' },
  { get: '/processcontrol?M1=255&M2=255' },
  {},
  { comment: '# swing the flipper' },
  { get: '/processcontrol?S1=90' },
  {},
  { comment: '# battery + telemetry' },
  { get: '/quickstatus' },
];

const CONFIGS = [
  { name: 'Flipper', note: 'servo-actuated arm' },
  { name: 'Spinner', note: 'weapon on a motor channel' },
  { name: 'Differential drive', note: 'two wheels, tank steering' },
  { name: 'Steering servo', note: 'car-style front axle' },
  { name: 'Classroom rover', note: 'no weapon, all learning' },
];

/* ----------------------------- page ----------------------------- */

export default function Home() {
  return (
    <Layout
      title="Affordable ESP32 battle bots"
      description="Kijani is an open-source ESP32 battle robot platform: dual motor drivers, servo outputs, LiPo charging and a browser-based control interface on a single affordable PCB."
    >
      <Hero
        eyebrow="Open-source combat robotics"
        title={
          <>
            One board.
            <br />
            Whole battle bot.
          </>
        }
        lead={
          <>
            Kijani puts motor drivers, servo outputs, LiPo charging, WiFi and a
            self-hosted control interface on a single ESP32 PCB — a full kit for
            around <strong>R600</strong>. Connect to its access point, open your
            browser, and drive.
          </>
        }
        actions={
          <>
            <Button to="/docs/intro">Build your bot</Button>
            <Button to="https://github.com/zaplakkies/kijani" variant="ghost" style={{ display: 'flex', alignItems: 'center', gap: '1ch' }}>
              <GithubLogoIcon size={24} />GitHub
            </Button>
          </>
        }
        finePrint="Firmware in C++ / PlatformIO · UI in plain HTML + JS · Unlicence"
        art={<BoardArt />}
        strip={<SpecStrip items={SPECS} />}
      />

      <main>
        <Section
          refdes="U1"
          eyebrow="Everything the robot needs is on the PCB"
          title="No module stack. No wiring loom. No transmitter."
        >
          <FeatureGrid features={FEATURES} />
        </Section>

        <Section dark>
          <Split>
            <div>
              <Refdes id="TX">If it speaks HTTP, it can drive</Refdes>
              <SectionTitle>The whole robot is an API</SectionTitle>
              <p>
                Every function — motors, servos, telemetry, settings, the
                filesystem — is an HTTP endpoint served by the board. Build a
                control page with sliders, wire up a gamepad, or script it from
                a laptop. The stock interface is just one client.
              </p>
              <Button to="/docs/api" variant="ghost-light">
                Read the API docs
              </Button>
            </div>
            <Terminal host="10.10.10.10" lines={API_LINES} />
          </Split>
        </Section>

        <Section refdes="J2" eyebrow="One platform, many robots" title="Pick your fight">
          <ConfigList items={CONFIGS} />
          <ConfigNote>
            The same board, firmware and web interface run all of them — the
            difference is what you bolt on and which endpoints your control page
            calls.
          </ConfigNote>
        </Section>

        <CtaBand
          title="Want a bot?"
          actions={
            <>
              <Button to="https://docs.google.com/forms/d/e/1FAIpQLSefcmKqDehQRFsC9WDCJS6LWhJCRrktLrYrf-59QBeeA0L29w/viewform">
                Register interest
              </Button>
              <Button to="/docs/intro" variant="ghost">
                Or build from source
              </Button>
            </>
          }
        >
          <p>
            We organise group buys by area to keep shipping cheap: an assembled
            PCB, battery, N20 motors and a servo for around R600. Tell us where
            you are and we&apos;ll be in touch when your region has enough
            builders.
          </p>
        </CtaBand>
      </main>
    </Layout>
  );
}
