// ==UserScript==
// @name         CloudMusicTest
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://music.163.com/
// @grant        none
// ==/UserScript==

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

let $menu = document.querySelector('div.wrap > ul.nav');

$menu.append(ui_element_creator('a',
    {id: 'load-all-post', href: 'javascript:;', event: {click: () => loadAllPost()}},
    'TestButton'));

function loadAllPost() {
    alert('Hello, world!');
}

let $title = document.querySelector('div.tit');
alert($title.getAttributeNames());
