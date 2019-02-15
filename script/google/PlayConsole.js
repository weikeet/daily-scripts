// ==UserScript==
// @name         GooglePlayTest
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://play.google.com/apps/publish/?account=8505122062204140606
// @grant        none
// ==/UserScript==

//alert('Hello, world!');
const ui_element_creator = (type, props, children) => {
    let elem = null;
    if (type === "text") {
        return document.createTextNode(props);
    } else {
        elem = document.createElement(type);
    }
    for (let n in props) {
        if (n === "style") {
            for (let x in props.style) {
                elem.style[x] = props.style[x];
            }
        } else if (n === "className") {
            elem.className = props[n];
        } else if (n === "event") {
            for (let x in props.event) {
                elem.addEventListener(x, props.event[x]);
            }
        } else {
            elem.setAttribute(n, props[n]);
        }
    }
    if (children) {
        if (typeof children === 'string') {
            elem.innerHTML = children;
        } else {
            for (let i = 0; i < children.length; i++) {
                if (children[i] != null) {
                    elem.appendChild(children[i]);
                }
            }
        }
    }
    return elem;
}

let $menu = document.querySelector('#TabPanel_tab_1_0');
$menu.append(ui_element_creator('a', {id: 'load-all-post', href: 'javascript:;', event: {click: () => loadAllPost()}},
    '[显示全部]'));

function loadAllPost() {
    alert('Hello, world!');
}

//与元数据块中的@grant值相对应，功能是生成一个style样式
//GM_addStyle('#down_video_btn{color:#fa7d3c;}');
