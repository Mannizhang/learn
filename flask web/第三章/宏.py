{%import 'macros.html' as macros%}
<ul>
    {%for comment in comments%}
        {{macors.render_comment(comment)}}
    {%endfor%}
<ul>