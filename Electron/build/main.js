/* dependencies */
const{ app, BrowserWindow } = require('electron')
const urlExist = require('url-exist');
const urlString = "http://127.0.0.1:5000/" 
var height = 500;
var width = 600;
const { spawn } = require('child_process');
var child = spawn('python', ['../Flask/Server/app.py']);


function createWindow() {
    let win = new BrowserWindow({
        width: width,
        height: height,
        webPreferences: {
            nodeIntegration: false
        }
    });

    win.loadFile('build/preload.html');
    exists(win);

    win.on('closed', function(){ 
    
        const { exec } = require('child_process'); 
    
        exec('taskkill /f /t /im python.exe', (err, stdout, stderr) => { 
    
          if (err) { 
    
            console.log(err) 
    
            return; 
          }
    
        }); 
    });
}



function exists(win) {
    (async () => { 

        const exists = await urlExist("http://127.0.0.1:5000/"); 
  
        // Handle result 
  
        win.loadURL('http://127.0.0.1:5000/') 
    })(); 
    return true
}


/* main loop */ 
app.whenReady().then(createWindow)




    

