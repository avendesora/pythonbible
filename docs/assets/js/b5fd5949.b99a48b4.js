(self.webpackChunkpythonbible_docs=self.webpackChunkpythonbible_docs||[]).push([[8134],{3905:function(e,r,t){"use strict";t.d(r,{Zo:function(){return l},kt:function(){return m}});var n=t(7294);function o(e,r,t){return r in e?Object.defineProperty(e,r,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[r]=t,e}function i(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function a(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?i(Object(t),!0).forEach((function(r){o(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}function s(e,r){if(null==e)return{};var t,n,o=function(e,r){if(null==e)return{};var t,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)t=i[n],r.indexOf(t)>=0||(o[t]=e[t]);return o}(e,r);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)t=i[n],r.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}var c=n.createContext({}),p=function(e){var r=n.useContext(c),t=r;return e&&(t="function"==typeof e?e(r):a(a({},r),e)),t},l=function(e){var r=p(e.components);return n.createElement(c.Provider,{value:r},e.children)},u={inlineCode:"code",wrapper:function(e){var r=e.children;return n.createElement(n.Fragment,{},r)}},f=n.forwardRef((function(e,r){var t=e.components,o=e.mdxType,i=e.originalType,c=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),f=p(t),m=o,b=f["".concat(c,".").concat(m)]||f[m]||u[m]||i;return t?n.createElement(b,a(a({ref:r},l),{},{components:t})):n.createElement(b,a({ref:r},l))}));function m(e,r){var t=arguments,o=r&&r.mdxType;if("string"==typeof e||o){var i=t.length,a=new Array(i);a[0]=f;var s={};for(var c in r)hasOwnProperty.call(r,c)&&(s[c]=r[c]);s.originalType=e,s.mdxType="string"==typeof e?e:o,a[1]=s;for(var p=2;p<i;p++)a[p]=t[p];return n.createElement.apply(null,a)}return n.createElement.apply(null,t)}f.displayName="MDXCreateElement"},1736:function(e,r,t){"use strict";t.r(r),t.d(r,{frontMatter:function(){return a},metadata:function(){return s},toc:function(){return c},default:function(){return l}});var n=t(2122),o=t(9756),i=(t(7294),t(3905)),a={sidebar_position:4},s={unversionedId:"howto-basics/format-scripture-references",id:"howto-basics/format-scripture-references",isDocsHomePage:!1,title:"Format Scripture References",description:"Given a list of normalized references, this feature formats them into a human-readable scripture reference string.",source:"@site/docs/howto-basics/format-scripture-references.md",sourceDirName:"howto-basics",slug:"/howto-basics/format-scripture-references",permalink:"/docs/howto-basics/format-scripture-references",editUrl:"https://github.com/avendesora/pythonbible/edit/main/pythonbible-docs/docs/howto-basics/format-scripture-references.md",version:"current",sidebarPosition:4,frontMatter:{sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Verse IDs -> References",permalink:"/docs/howto-basics/convert-verse-ids-to-references"},next:{title:"Format Scripture Text",permalink:"/docs/howto-basics/format-scripture-text"}},c=[],p={toc:c};function l(e){var r=e.components,t=(0,o.Z)(e,["components"]);return(0,i.kt)("wrapper",(0,n.Z)({},p,t,{components:r,mdxType:"MDXLayout"}),(0,i.kt)("p",null,"Given a list of normalized references, this feature formats them into a human-readable scripture reference string."),(0,i.kt)("p",null,"It sorts the list so that the references appear in the order they would in the Bible.\nIt also combines verses into ranges when possible."),(0,i.kt)("p",null,"For example:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},'import pythonbible as bible\n\ntext = "My favorite verses are Philippians 4:8, Isaiah 55:13, and Philippians 4:4-7."\nreferences = bible.get_references(text)\nformatted_reference = bible.format_scripture_references(references)\n')),(0,i.kt)("p",null,"The resulting formatted reference should be:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"'Isaiah 55:13;Philippians 4:4-8'\n")))}l.isMDXComponent=!0}}]);