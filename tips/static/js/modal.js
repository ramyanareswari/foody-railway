
// ======== untuk get data dari submit form ========
async function getArticleData() {
    return $.get("/tips/json/", (respond) => respond.json())
  }

  
// ======== untuk post data dari hasil submit form ========
async function addArticle() {
document.getElementById("article-container").innerHTML = ""
const data = await getArticleData()
let htmlString = ``
data.forEach((e) => {
    htmlString += 
    `
    <div class="card mb-3">
        <div class="row">
        
            <div class="col-md-4">
                <div class="position-relative">
                <img
                    height="230px"
                    src=${e.fields.image}
                    class="rounded w-100"
                >
                </div>
            </div>

            <div class="col-md-8">
                <div class="mt-2">
                <div class="d-flex justify-content-between align-items-center">
                    <h5 class="mb-1">${e.fields.title}</h5>
                </div>
                <div class="d-flex justify-content-md-start justify-content-between views-content mt-2">
                    <div class="d-flex flex-row align-items-center"><span class="ms-1 views">${e.fields.publish}</span> </div>
                </div>
                <p class="text-dark mt-3 px-3">${e.fields.content}</p>
                <a
                    class="btn btn-sm btn-dark"
                    target="_blank"
                    href="${e.pk}"
                >Baca lebih banyak</a>
                </div>
            </div>
        </div>
    </div>
    `   
})
document.getElementById("article-container").innerHTML = htmlString
}

addArticle()

$(document).on('submit', '#createForm', function(e){
    e.preventDefault;

    $.ajax({
      type:'POST',
      url:"/tips/add-article/",
      data:{
        title:$('#id_title').val(),
        content:$('#id_content').val(),
        publish:$('#initial-id_publish').val(),
        image:$('#id_image').val(),
        csrfmiddlewaretoken:'{{ csrf_token }}',
      },
      dataType: 'json',
    });
  });

