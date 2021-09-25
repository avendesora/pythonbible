(self.webpackChunkpythonbible_docs=self.webpackChunkpythonbible_docs||[]).push([[5991],{3905:function(e,n,t){"use strict";t.d(n,{Zo:function(){return p},kt:function(){return f}});var r=t(7294);function o(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function i(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function a(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?i(Object(t),!0).forEach((function(n){o(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,o=function(e,n){if(null==e)return{};var t,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||(o[t]=e[t]);return o}(e,n);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}var l=r.createContext({}),c=function(e){var n=r.useContext(l),t=n;return e&&(t="function"==typeof e?e(n):a(a({},n),e)),t},p=function(e){var n=c(e.components);return r.createElement(l.Provider,{value:n},e.children)},u={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},d=r.forwardRef((function(e,n){var t=e.components,o=e.mdxType,i=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),d=c(t),f=o,m=d["".concat(l,".").concat(f)]||d[f]||u[f]||i;return t?r.createElement(m,a(a({ref:n},p),{},{components:t})):r.createElement(m,a({ref:n},p))}));function f(e,n){var t=arguments,o=n&&n.mdxType;if("string"==typeof e||o){var i=t.length,a=new Array(i);a[0]=d;var s={};for(var l in n)hasOwnProperty.call(n,l)&&(s[l]=n[l]);s.originalType=e,s.mdxType="string"==typeof e?e:o,a[1]=s;for(var c=2;c<i;c++)a[c]=t[c];return r.createElement.apply(null,a)}return r.createElement.apply(null,t)}d.displayName="MDXCreateElement"},9318:function(e,n,t){"use strict";t.r(n),t.d(n,{frontMatter:function(){return a},metadata:function(){return s},toc:function(){return l},default:function(){return p}});var r=t(2122),o=t(9756),i=(t(7294),t(3905)),a={sidebar_position:2},s={unversionedId:"howto-advanced/multi-book-references",id:"howto-advanced/multi-book-references",isDocsHomePage:!1,title:"Multi Book References",description:"It is possible for a single reference to be a range than spans more than one book of the Bible.",source:"@site/docs/howto-advanced/multi-book-references.md",sourceDirName:"howto-advanced",slug:"/howto-advanced/multi-book-references",permalink:"/docs/howto-advanced/multi-book-references",editUrl:"https://github.com/avendesora/pythonbible/edit/main/pythonbible-docs/docs/howto-advanced/multi-book-references.md",version:"current",sidebarPosition:2,frontMatter:{sidebar_position:2},sidebar:"tutorialSidebar",previous:{title:"Single Chapter Books",permalink:"/docs/howto-advanced/single-chapter-books"},next:{title:"Book Groups",permalink:"/docs/howto-advanced/book-groups"}},l=[{value:"Finding References",id:"finding-references",children:[]},{value:"Converting References to Verse IDs",id:"converting-references-to-verse-ids",children:[]},{value:"Converting Verse IDs to References",id:"converting-verse-ids-to-references",children:[]},{value:"Formatting References for Print/Display",id:"formatting-references-for-printdisplay",children:[{value:"Always Include Chapter Numbers",id:"always-include-chapter-numbers",children:[]}]}],c={toc:l};function p(e){var n=e.components,t=(0,o.Z)(e,["components"]);return(0,i.kt)("wrapper",(0,r.Z)({},c,t,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("p",null,"It is possible for a single reference to be a range than spans more than one book of the Bible."),(0,i.kt)("p",null,"For example, the following references are all equally referencing the entire first five books of the Bible:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Genesis - Deuteronomy"),(0,i.kt)("li",{parentName:"ul"},"Genesis 1 - Deuteronomy 34"),(0,i.kt)("li",{parentName:"ul"},"Genesis 1:1 - Deuteronomy 34:12")),(0,i.kt)("h2",{id:"finding-references"},"Finding References"),(0,i.kt)("p",null,"When parsing a given text to find all the references contained within, if we find a ranged reference like those above that span multiple books of the Bible, we should parse that into a single normalized reference that includes the optional ",(0,i.kt)("inlineCode",{parentName:"p"},"end_book")," attribute."),(0,i.kt)("p",null,'For example, "Genesis - Deuteronomy" vs "Genesis;Exodus;Numbers;Leviticus;Deuteronomy":'),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Code"',title:'"Code"'},'import pythonbible as bible\n\nreferences = bible.get_references("Genesis - Deuteronomy")\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Result"',title:'"Result"'},"[\n    NormalizedReference(\n        book=<Book.GENESIS: 1>, \n        start_chapter=1, \n        start_verse=1, \n        end_chapter=34, \n        end_verse=12, \n        end_book=<Book.DEUTERONOMY: 5>\n    )\n]\n")),(0,i.kt)("p",null,"If rather than using the range, the text specified each book of the Bible separated by a comma or semi-colon (or just about anything), then the result would be a list of five normalized references, one for each of the five books referenced."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Code"',title:'"Code"'},'import pythonbible as bible\n\nreferences = bible.get_references("Genesis;Exodus;Leviticus;Numbers;Deuteronomy")\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Result"',title:'"Result"'},"[\n    NormalizedReference(\n        book=<Book.GENESIS: 1>,\n        start_chapter=1,\n        start_verse=1,\n        end_chapter=50,\n        end_verse=26,\n        end_book=None\n    ),\n    NormalizedReference(\n        book=<Book.EXODUS: 2>,\n        start_chapter=1,\n        start_verse=1,\n        end_chapter=40,\n        end_verse=38,\n        end_book=None\n    ),\n    NormalizedReference(\n        book=<Book.LEVITICUS: 3>,\n        start_chapter=1,\n        start_verse=1,\n        end_chapter=27,\n        end_verse=34,\n        end_book=None\n    ),\n    NormalizedReference(\n        book=<Book.NUMBERS: 4>,\n        start_chapter=1,\n        start_verse=1,\n        end_chapter=36,\n        end_verse=13,\n        end_book=None\n    ),\n    NormalizedReference(\n        book=<Book.DEUTERONOMY: 5>,\n        start_chapter=1,\n        start_verse=1,\n        end_chapter=34,\n        end_verse=12,\n        end_book=None\n    )\n]\n")),(0,i.kt)("p",null,"That list can optionally be optimized by converting it to verse ids and then back into references if so desired."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Code"',title:'"Code"'},'import pythonbible as bible\n\nreferences = bible.get_references("Genesis;Exodus;Leviticus;Numbers;Deuteronomy")\nverse_ids = bible.convert_references_to_verse_ids(references)\nreferences = bible.convert_verse_ids_to_references(verse_ids)\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Result"',title:'"Result"'},"[\n    NormalizedReference(\n        book=<Book.GENESIS: 1>, \n        start_chapter=1, \n        start_verse=1, \n        end_chapter=34, \n        end_verse=12, \n        end_book=<Book.DEUTERONOMY: 5>\n    )\n]\n")),(0,i.kt)("p",null,"That optimization is optional as it can degrade performance for processing large ranges if that particular optimization is not necessary. This optimization will be run automatically when the list of references is formatted into a Scripture reference string."),(0,i.kt)("h2",{id:"converting-references-to-verse-ids"},"Converting References to Verse IDs"),(0,i.kt)("p",null,"Whether a multi book range reference is in a single normalized reference or a list of one normalized reference for each book does not affect the results of converting that reference into a list of verse ids."),(0,i.kt)("h2",{id:"converting-verse-ids-to-references"},"Converting Verse IDs to References"),(0,i.kt)("p",null,"When converting a list of verse ids into a list of references, multi book range references will always be optimized into a single normalized reference when possible."),(0,i.kt)("h2",{id:"formatting-references-for-printdisplay"},"Formatting References for Print/Display"),(0,i.kt)("p",null,"As mentioned earlier, when formatting references for print/display, pythonbible always optimizes the list of references into as few references as possible by using multi book range references."),(0,i.kt)("p",null,"By default, chapter numbers will not be included when the entire book is included in the reference."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Code"',title:'"Code"'},'import pythonbible as bible\n\nreferences = bible.get_references("Genesis - Deuteronomy")\nreference_text = bible.format_scripture_references(references)\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Result"',title:'"Result"'},"'Genesis - Deuteronomy'\n")),(0,i.kt)("h3",{id:"always-include-chapter-numbers"},"Always Include Chapter Numbers"),(0,i.kt)("p",null,"If you want to force pythonbible to include the chapter numbers even when the entire book is covered by the reference, you can use the optional ",(0,i.kt)("inlineCode",{parentName:"p"},"always_include_chapter_numbers")," optional parameter of the ",(0,i.kt)("inlineCode",{parentName:"p"},"format_scripture_references")," or ",(0,i.kt)("inlineCode",{parentName:"p"},"format_single_reference")," functions, setting that optional parameter to be ",(0,i.kt)("inlineCode",{parentName:"p"},"True"),"."),(0,i.kt)("p",null,"For example:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Code"',title:'"Code"'},'import pythonbible as bible\n\nreferences = bible.get_references("Genesis - Deuteronomy")\nreference_text = bible.format_scripture_references(\n    references,\n    always_include_chapter_numbers=True\n)\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Result"',title:'"Result"'},"'Genesis 1:1 - Deuteronomy 34:12'\n")))}p.isMDXComponent=!0}}]);