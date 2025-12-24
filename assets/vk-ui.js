(function(){
  var t=document.querySelector('.nav-toggle'),n=document.querySelector('.site-nav');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o);});}
  var f=null;
  if(f){f.addEventListener('submit',function(e){e.preventDefault();
    if(!f.checkValidity()){f.reportValidity();return;}
    f.reset();document.getElementById('form-note').hidden=false;});}
})();
