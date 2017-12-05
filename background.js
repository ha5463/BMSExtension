
var contextList = ["selection", "image", "link", "page"];

for(i=0;i<contextList.length;i++){
    var context = contextList[i];
    var titleX = "Social Toolkit: share this "+context;

    chrome.contextMenus.create({
        title: titleX,
        contexts:[context], 
        onclick: myFunction,
        id: context
    });
}
function myFunction(data, tab){
    switch(data.menuItemId){
        case 'selection':  chrome.windows.create({url: "https://www.twitter.com/intent/tweet?text="+encodeURIComponent(data.selectionText), type: "panel" });
        break;
        case 'link' :  chrome.windows.create({url: "https://www.twitter.com/intent/tweet?url="+encodeURIComponent(data.linkUrl), type: "panel" });
        break;
        case 'image':  chrome.windows.create({url: "https://www.twitter.com/intent/tweet?url="+encodeURIComponent(data.srcUrl),type: "panel"});
        break;
        case 'page': chrome.windows.create({url: "https://www.twitter.com/intent/tweet?text="+encodeURIComponent(tab.title)+"&url="+(data.pageUrl), type:"panel" });
        break;
    }  
}