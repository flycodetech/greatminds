console.log("hello world from popup")

function setBadgeText(enabled) {
    const text: string = enabled ? "NO" : "OFF"
    void chrome.action.setBadgeText({ text: text })

}
// handle the on / off switch

const checkbox: HTMLElement =  document.getElementBy 