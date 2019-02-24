$(document).ready(function() {

  $("#questions_form").on("submit", function(event) {
    $.ajax({
      data: {
        test_questions: $("#test_questions").val()
      },
      type: 'POST',
      url: '/process'
    })
    .done(function(data) {
      $("#shuffled_questions").text(data.questions);
    });

    event.preventDefault();
  });

});
