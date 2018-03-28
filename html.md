# web HTML指南
## 一定要以`<doctype>`开头
每个页面都要从doctype开始。任何时候都要使用<!doctyoe html>，除非你在写HTML4.01或者XHTML
## `html`元素，不能没有它
<html>元素必须时web页面的最顶端或者根元素。所以在doctype后面，由<html>标记开始到</html>标记结束。页面中其他内容都嵌套在这个元素中。
## 使用<head>和<body>编写更好的html
只有<head>和<body>元素能直接放在<html>元素中。这说明，所有其他元素都必须放在<head>或<body>中
## <head>中指定字符编码
在<head>中包含一个<meta charset="utf-8">标记。浏览器会正确的对你的html进行编码。
## <title>标签
在<head>中加入<title>标签这才是一个标准的html
# 基本块级标签
## `h`标签
<hn>标签共有1-6依次减小代表6个标题前后隔行
```html
<h1>标题</h1>
<h1>标题</h1>
<h1>标题</h1>
<h1>标题</h1>
<h1>标题</h1>
<h1>标题</h1>
```
## `p`标签
<p>标签是段落标签可以自动换行，并且浏览器会自动地在段落的前后添加空行。
```html
<p>hello world!!</p>
<p>hello html!!</p>
```
## <hr>水平线标签
<hr>标签默认宽度整个网页黑色宽度2px
color： 改变颜色
width: 长度
size: 宽度
# 常用于布局的块级标签
## 有序列表标签`ol`
有序列表是一个项目的列表，列表项目默认使用数字进行标记。
有序列表始于 <ol> 标签。每个列表项始于 <li> 标签。
```html
<ol>
  <li>开始</li>
  <li>游戏</li>
  <li>结束</li>
</ol>
```
## 无序列表
无序列表是一个项目的列表，列表项目默认使用小圆点进行标记。
```html
<ul>
  <li>开始</li>
  <li>游戏</li>
  <li>结束</li>
</ul>
```
修改<ul>`type`更改项目样式
square 正方形
circle 空心圆
disc 实心圆 默认
## 描述标签<dl>
<dl> 标签定义一个描述列表。
<dl> 标签与 <dt> （定义项目/名字）和 <dd> （描述每一个项目/名字）一起使用。
```html
<dl>
  <dt>Coffee</dt>
    <dd>Black hot drink</dd>
  <dt>Milk</dt>
    <dd>White cold drink</dd>
</dl>
```
# 行级标签
## <img>标签
<img> 标签定义 HTML 页面中的图像。
<img> 标签有两个必需的属性：src 和 alt。
src 图片的连接路径 alt 属性用来为图像定义一串预备的可替换的文本。
通过在 <a> 标签中嵌套 <img> 标签，给图像添加到另一个文档的链接。
```html
<img src="smiley-2.gif" alt="Smiley face" width="42" height="42">
```
## <span>范围样式标签
<span> 用于对文档中的行内元素进行组合。
<span> 标签提供了一种将文本的一部分或者文档的一部分独立出来。
```html
<p>我的母亲有 <span style="color:blue">蓝色</span> 的眼睛。</p>
```
## 












