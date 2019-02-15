// ==UserScript==
// @name         BaiduTest
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Weicools
// @match        *://pan.baidu.com/disk/home*
// @match        *://yun.baidu.com/disk/home*
// @match        *://pan.baidu.com/s/*
// @match        *://yun.baidu.com/s/*
// @match        *://pan.baidu.com/share/link?*
// @match        *://yun.baidu.com/share/link?*
// @match        *://eyun.baidu.com/s/*
// @match        *://eyun.baidu.com/enterprise/share/link?*
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

let $menu = document.querySelector('div.module-aside[node-type=knNaPx] > ul.fOHAbxb');
$menu.append(ui_element_creator('a',
    {id: 'load-all-post', href: 'javascript:;', event: {click: () => showDialog()}},
    'TestButton'));

function showDialog() {
    alert('Hello, world!');
}