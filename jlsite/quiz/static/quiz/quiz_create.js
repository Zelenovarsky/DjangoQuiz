   $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });


    String.prototype.format = function () {
        var args = arguments;
        return this.replace(/\{(\d+)\}/g, function (m, n) {
            return args[n];
        });
    };

    var count = 0;

    function addQuestion(questionType) {
        var questionId = 'question' + count;
        if (questionType != 'text') {
            var inputArea = '<div class="input-group mb-3">\n' +
                '  <div class="input-group-prepend">\n' +
                '    <span class="input-group-text" id="basic-addon3">question text</span>\n' +
                '  </div>\n' +
                '  <input type="text" class="question form-control" id="basic-url" aria-describedby="basic-addon3">\n' +
                '</div>'

            var question = '<div id = \"{0}\" class = \"question\" type = \"{1}\">{2}  \
    <button class=\"btn btn-primary\"  id = \"answerAdd\" onclick = \"addAnswer(\'{0}\',\'{1}\')\">add answer</button> </div><hr>'.format(questionId, questionType,inputArea);
        } else {
            var question = '<div id = \"{0}\"  type = \"{1}\" class = \"question\">open question text <textarea type=\"open\"  class =\"question\"> </textarea> <br> \
      Answer, answer text <input type=\"text\" class=\"answerText\"> </div> <hr>'.format(questionId, questionType)
        }

        $("#quizContainer").append(question);
        count++;
    }

    function addAnswer(questionId, questionType) {

        var question = '<div>Answer, answer text <input type=\"text\" class=\"answerText\"> is correct? <input class = \"answer\" type=\"{0}\" name=\"{1}\"> </div>'.format(questionType, questionId);

        $('#' + questionId).append(question);

    }


    function quizJSON() {
        var quiz = {};
        quizname = $('#quizName').val();
        var quizDict = [];
        var rightAns = [];

        $('div.question').each(function () {
            var question = $(this).find(".question");
            var current = question.val();
            quiz[current] = {};
            quiz[current]['type'] = $(this).attr('type');
            quiz[current]['answers'] = [];
            quiz[current]['correctAnswers'] = [];

            $(this).find('.answer').each(function () {
                if ($(this).is(':checked')) {
                    quiz[current]['correctAnswers'].push($(this).closest('div').find(".answerText").val())
                }
            })


            $(this).find('.answerText').each(function () {
                if (question.attr('type') === 'open') {
                    quiz[current]['correctAnswers'].push($(this).val());
                }
                quiz[current]['answers'].push($(this).val());
            });
        })
        return [quizname, JSON.stringify(quiz)];
    }

    function sendRequest() {
        var quizinstance = quizJSON();
        alert(quizinstance);
        $.ajax({
            type: 'POST',
            url: '/quiz/save',
            data: {
                quiz_data: quizinstance[1],
                quiz_name: quizinstance[0],
            },
            success: function (response) {
                console.log(response);

            }
        });

    }