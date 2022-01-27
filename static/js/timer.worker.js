var time = 0
var timerID = undefined

self.onmessage = function(msg) {
  switch (msg.data) {
  case 'stop':
    if (timerID !== undefined) {
      clearInterval(timerID)
      timerID = undefined
    }
    break
    
  case 'go':
    if (timerID === undefined) {
      timerID = setInterval(() => { updateTime() }, 1000)
    }
    break

  default:
    time = msg.data
    break
  }
}

function updateTime() {
  time = time > 0 ? time - 1 : 'DONE'
  self.postMessage(time);
  if (time < 0) {
    if (timerID !== undefined) {
      clearInterval(timerID)
      timerID = undefined
    }
  }
}
