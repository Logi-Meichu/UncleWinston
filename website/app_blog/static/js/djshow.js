!document.addEventListener('keydown', function(event) {
    // if(event.keycode == 37) {
    //     var oShell = new ActiveXObject("Shell.Application");
    //     var commandtoRun = "Logi_Led.exe"; 
    //     oShell.ShellExecute(commandtoRun,"","","open","1");
    // }
    if(event.keycode == 37) {
        alert('Left was pressed');
    }
    else if(event.keycode == 39) {
        alert('Right was pressed');
    }
});