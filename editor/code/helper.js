function download() {
  var a = document.createElement('a');
  a.href = 'data:text/plain;base64,' +
    btoa(document.getElementById('content_python').innerHTML);
  a.textContent = 'download';
  a.download = 'blockCode.py';
  a.click();
  downloadXML();
}

function downloadXML(){
  var a = document.createElement('a');
  a.href = 'data:text/plain;base64,'+
    btoa(document.getElementById('content_xml').value);
  a.textContent = 'download';
  a.download = 'blockCode.xml';
  a.click();
}

function upload(){
  document.getElementById('file').addEventListener('change', readFile, false);
  function readFile (evt) {
      var files = evt.target.files;
      var file = files[0];
      var reader = new FileReader();
      reader.onload = function(e) {
        //console.log(e.target.result);
        document.getElementById('content_xml').value = e.target.result;
      }
      reader.readAsText(file)
   }
 }
