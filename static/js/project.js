var timer_data = {
  project_id: undefined,
  row: undefined,
  column: undefined,
  duration: undefined,
  url: undefined,
}

const el = document.getElementById('timer-data')
if (el) {
  timer_data = JSON.parse(el.textContent)  
}

function formatTime(val) {
  var result = val.toString()
  if (result.length == 1) {
    result = '0' + result
  }
  return result
}

function formatMinutes(s) {
  return formatTime(Math.floor(s / 60))
}

function formatSeconds(s) {
  return formatTime(s % 60)
}

function setupTimer() {
  return {
    time: timer_data.duration,
    minutes: formatMinutes(timer_data.duration),
    seconds: formatSeconds(timer_data.duration),
    start: undefined,
    timer: new Worker('/static/js/timer.worker.js'),
    running: false,
    finished: false,
    label: 'Start',
    sound: new Audio('/static/sounds/alarm.wav'),

    resetTimer: function() {
      const self = this
      
      self.timer.postMessage('stop')
      if (confirm('Are you sure you want to reset the timer?')) {
        self.timer.postMessage(timer_data.duration)
        self.time = timer_data.duration
        self.minutes = formatMinutes(self.time)
        self.seconds = formatSeconds(self.time)
        self.start = undefined
        self.label = 'Start'
        self.running = false
      } else {
        if (self.running) self.timer.postMessage('go')
      }
    },
    
    cancelBlock: function() {
      const self = this

      self.timer.postMessage('stop')
      if (confirm('Are you sure you want to cancel this block?')) {
        window.location.href = '/'
      } else {
        if (self.running) self.timer.postMessage('go')
      }
    },

    addBlock: function() {
      const self = this
      
      if (self.start === undefined) {
        self.start = new Date()
      }
      self.saveBlock()
    },
    
    saveBlock: function() {
      const self = this
      
      var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
      var note = document.getElementsByName('note')[0].value
      const data = {
        project_id: timer_data.project_id,
        row: timer_data.row,
        column: timer_data.column,
        start: self.start.toISOString(),
        duration: timer_data.duration,
        note: note,
      }
      const body = JSON.stringify(data)
      fetch(timer_data.url,
            { method: 'POST',
              mode: 'same-origin',
              headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
              },
              body: body,
            })
        .then(response => {
          if (response.status === 200) {
            window.location.href = '/'
          } else {
            alert('Something went wrong!')
          }
        })
    },
    
    blockFinished: function() {
      const self = this

      self.timer.postMessage('stop')
      self.running = false
      self.sound.play()
      alert('Timer finished! Saving...')
      self.sound.pause()
      self.sound.load()
      self.saveBlock()
    },

    startStopTimer: function() {
      const self = this
      
      self.timer.onmessage = function(msg) {
        self.time = msg.data
        if (self.time == 0) self.blockFinished()
        if (self.time > 0) self.time -= 1
        self.minutes = formatMinutes(self.time)
        self.seconds = formatSeconds(self.time)
      }

      self.running = !self.running
      if (self.running) {
        if (self.start === undefined) {
          self.start = new Date()
          self.timer.postMessage(timer_data.duration)
        }
        self.timer.postMessage('go')
      } else {
        self.timer.postMessage('stop')
      }

      self.label = self.running ? 'Pause' : 'Resume'
    }
  }
}
