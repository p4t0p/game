(this.webpackJsonpchess=this.webpackJsonpchess||[]).push([[0],{161:function(e,t,n){e.exports=n(456)},455:function(e,t,n){},456:function(e,t,n){"use strict";n.r(t);n(162),n(164),n(165),n(166),n(167),n(168),n(169),n(170),n(171),n(172),n(173),n(174),n(175),n(176),n(177),n(178),n(179),n(180),n(181),n(182),n(183),n(184),n(185),n(186),n(187),n(188),n(189),n(74),n(190),n(191),n(192),n(193),n(194),n(195),n(196),n(197),n(198),n(199),n(200),n(201),n(202),n(203),n(204),n(205),n(206),n(207),n(208),n(210),n(211),n(213),n(214),n(215),n(216),n(103),n(217),n(218),n(219),n(220),n(221),n(222),n(223),n(224),n(225),n(226),n(227),n(228),n(229),n(230),n(231),n(232),n(233),n(234),n(235),n(236),n(237),n(238),n(239),n(240),n(241),n(242),n(243),n(244),n(245),n(246),n(247),n(248),n(249),n(250),n(251),n(252),n(253),n(254),n(255),n(256),n(257),n(258),n(259),n(260),n(261),n(262),n(263),n(264),n(265),n(266),n(267),n(268),n(269),n(271),n(272),n(273),n(274),n(275),n(276),n(277),n(279),n(280),n(281),n(282),n(283),n(284),n(285),n(286),n(287),n(288),n(289),n(290),n(291),n(292),n(293),n(146),n(294),n(295),n(296),n(297),n(147),n(298),n(299),n(300),n(301),n(302),n(303),n(304),n(305),n(306),n(307),n(308),n(309),n(310),n(311),n(312),n(313),n(314),n(315),n(316),n(317),n(318),n(319),n(320),n(321),n(322),n(323),n(324),n(325),n(326),n(327),n(328),n(329),n(330),n(331),n(332),n(333),n(334),n(335),n(336),n(337),n(338),n(339),n(340),n(341),n(342),n(343),n(344),n(345),n(346),n(347),n(348),n(349),n(350),n(351),n(352),n(353),n(354),n(355),n(356),n(113),n(357),n(358),n(359),n(360),n(361),n(362),n(363),n(364),n(365),n(366),n(367),n(368),n(369),n(370),n(371),n(373),n(374),n(375),n(376),n(377),n(378),n(379),n(380),n(381),n(382),n(383),n(384),n(385),n(386),n(387),n(388),n(389),n(390),n(391),n(392),n(393),n(394),n(395),n(396),n(397),n(399),n(400),n(401),n(402),n(403),n(404),n(405),n(406),n(407),n(408),n(409),n(410),n(411),n(412),n(413),n(414),n(415),n(416),n(417),n(418),n(419),n(420),n(421),n(422),n(423),n(424),n(425),n(426),n(427),n(428),n(429),n(430),n(433),n(434),n(435),n(436),n(437),n(438),n(439),n(440),n(441),n(442),n(443),n(444),n(445),n(446),n(447),n(448),n(450),n(157);var r=n(24),c=n.n(r),o=n(159),a=n(160),i=n(70);n(455);function l(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function u(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?l(n,!0).forEach((function(t){Object(a.a)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):l(n).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e){var t=e.field,n=e.makeMove,r=e.turn,o=c.a.useState(null),a=Object(i.a)(o,2),l=a[0],u=a[1],s=t.map((function(e,t){return c.a.createElement("div",{className:"Row",key:"r"+t},e.map((function(e,o){var a="C.".concat(t,".").concat(o),s=t%2?o%2?"white":"black":o%2?"black":"white",f="Cell ".concat(e&&e.kind," ").concat(e&&e.color," bg-").concat(s," ").concat(l&&l[0]===a?"active":"");return c.a.createElement("div",{key:a,cid:a,className:f,onClick:function(){return function(e,t){if((l||t)&&(l||t.color===r))if(l&&e===l[0])u(null);else if(l){var c=e.split(".").map(Number),o=Object(i.a)(c,3),a=(o[0],o[1]),s=o[2];n({x:l[1].x,y:l[1].y},{x:s,y:a}),u(null)}else u([e,t])}(a,e)}})})))}));return c.a.createElement("div",{className:"Field ".concat(l&&"active"," turn-").concat(r)},s)}function f(){var e=c.a.useState(localStorage.getItem("data")),t=Object(i.a)(e,2),n=t[0],r=t[1],o=c.a.useState(!Boolean(n)),a=Object(i.a)(o,2),l=a[0],f=a[1],p=function(){f(!0),fetch("http://localhost:8080/game",{method:"POST"}).then((function(e){return e.json()})).then((function(e){r(e),f(!1)})).catch((function(e){console.error(e)}))};return c.a.useEffect((function(){n&&null!==n||p()}),[]),l?c.a.createElement("h1",null,"Loading"):c.a.createElement("div",{className:"AppContainer"},c.a.createElement("button",{onClick:p},"\u041d\u043e\u0432\u0430\u044f \u0438\u0433\u0440\u0430"),c.a.createElement(s,{field:n.field,turn:n.turn,makeMove:function(e,t){f(!0),fetch("http://localhost:8080/move",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(u({},n,{move:{from:e,to:t}}))}).then((function(e){return e.json()})).then((function(e){e.error?alert(e.error):r(e),f(!1)}))}}))}n.d(t,"renderApp",(function(){return m}));var p="application_root";function m(){Object(o.render)(c.a.createElement(f,null),document.getElementById(p))}m()}},[[161,1,2]]]);
//# sourceMappingURL=main.23ce67e8.chunk.js.map