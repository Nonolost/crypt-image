<form id="upload-file" role="form" action="sendQuestions" method="post" enctype="multipart/form-data">
<div class="modal-body">
    <label for="file"><b>Upload packet here</b></label>
    <input type="file" name="file">
    <p class="help-block">Upload a .pdf or .docx file you want to read.</p>
</div>
<div class="modal-footer">
    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
    <button id="upload-file-btn" type="button" class="btn btn-primary" data-dismiss="modal" value="Upload">Upload</button>
</div>
</form>

<script>

$(function() {
$('#upload-file-btn').click(function() {
    var form_data = new FormData($('#upload-file')[0]);
    $.ajax({
        type: 'POST',
        url: 'encrypt.py',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        async: false,
        success: function(data) {
            console.log('Success!');
        },
    });
});
});