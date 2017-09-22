function progress(){
    var a = document.getElementByTd('progress-bar');
    var percent = document.getElementByTd('percentCount');
    var counter = 5;
    var progress 5;
    var id = setInterval(frame, 10);

    function frame(){
        if(progress == 100 && counter == 100){
            clearInterval(id);
        }
        else{
            progress += 5;
            counter += 1;
            a.style.with = progress + 'px';
            percent.innerHTML = counter + '%';
        }
    }
}

progress();