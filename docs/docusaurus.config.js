// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
	title: 'Kijani',
	tagline: 'An affordable custom ESP32-based robot designed for custom remote-controlled projects.',
	favicon: 'img/favicon.ico',

	// Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
	future: {
		v4: true, // Improve compatibility with the upcoming Docusaurus v4
	},

	url: 'https://ithegi.github.io',
	baseUrl: '/Kijani/',
	organizationName: 'Ithegi',
	projectName: 'Kijani',
	deploymentBranch: 'gh-pages',

	onBrokenLinks: 'throw',

	// Even if you don't use internationalization, you can use this field to set
	// useful metadata like html lang. For example, if your site is Chinese, you
	// may want to replace "en" with "zh-Hans".
	i18n: {
		defaultLocale: 'en',
		locales: ['en'],
	},

	presets: [
		[
			'classic',
			{
				docs: false, // disable default docs plugin
				blog: {
					showReadingTime: true,
					feedOptions: {
						type: ['rss', 'atom'],
						xslt: true,
					},
					editUrl: 'https://github.com/Ithegi/Kijani/tree/main/packages/create-docusaurus/templates/shared/',
					onInlineTags: 'warn',
					onInlineAuthors: 'warn',
					onUntruncatedBlogPosts: 'warn',
				},
				theme: {
					customCss: './src/css/custom.css',
				},
			},
		],
	],

	plugins: [
		[
			'@docusaurus/plugin-content-docs',
			{
				id: 'software',
				path: 'docs/software',
				routeBasePath: 'docs/software',
				sidebarPath: './sidebars/software.js',
			},
		],
		[
			'@docusaurus/plugin-content-docs',
			{
				id: 'hardware',
				path: 'docs/hardware',
				routeBasePath: 'docs/hardware',
				sidebarPath: './sidebars/hardware.js',
			},
		],
	],

	themeConfig:
	/** @type {import('@docusaurus/preset-classic').ThemeConfig} */
	({
		//Kept here to make future announcements simpler
		//announcementBar: {
		//id: 'support_us', // change when you want to dismiss/reset it
		//content:
		//'🚧 This site is under active development. Expect changes.',
		//backgroundColor: '#fec901',
		//textColor: '#010000',
		//isCloseable: true,
		//},
		// Replace with your project's social card
		image: 'img/docusaurus-social-card.jpg',
		colorMode: {
			respectPrefersColorScheme: true,
		},
		navbar: {
			title: 'Kijani',
			logo: {
				alt: 'Kijani Logo',
				src: 'img/logo.svg',
			},
			items: [
				{
					to: '/',
					label: 'Home',
					position: 'left',
				},
				{
					label: 'Docs',
					position: 'left',
					items: [
						{
							type: 'docSidebar',
							sidebarId: 'softwareSidebar',
							docsPluginId: 'software',
							label: 'Software',
						},
						{
							type: 'docSidebar',
							sidebarId: 'hardwareSidebar',
							docsPluginId: 'hardware',
							label: 'Hardware',
						},
					],
				},
				{to: '/blog', label: 'Blog', position: 'left'},
				{
					href: 'https://github.com/Ithegi/Kijani',
					label: 'GitHub',
					position: 'right',
				},
			],
		},
		footer: {
			style: 'dark',
			links: [
				{
					title: 'Docs',
					items: [
						{
							label: 'Software',
							to: '/docs/software',
						},
						{
							label: 'Hardware',
							to: '/docs/hardware',
						},
					],
				},
				{
					title: 'Community',
					items: [
						{
							label: 'Stack Overflow',
							href: 'https://stackoverflow.com/questions/tagged/docusaurus',
						},
						{
							label: 'Discord',
							href: 'https://discordapp.com/invite/docusaurus',
						},
						{
							label: 'X',
							href: 'https://x.com/docusaurus',
						},
					],
				},
				{
					title: 'Community',
					items: [
						{
							label: 'Stack Overflow',
							href: 'https://stackoverflow.com/questions/tagged/docusaurus',
						},
						{
							label: 'Discord',
							href: 'https://discordapp.com/invite/docusaurus',
						},
						{
							label: 'X',
							href: 'https://x.com/docusaurus',
						},
					],
				},
				{
					title: 'More',
					items: [
						{
							label: 'Blog',
							to: '/blog',
						},
						{
							label: 'GitHub',
							href: 'https://github.com/Ithegi/Kijani',
						},
					],
				},
			],
			copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
		},
		prism: {
			theme: prismThemes.github,
			darkTheme: prismThemes.dracula,
		},
	}),
};

export default config;
