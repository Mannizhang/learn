# 条件控制语句：
{% if user %}
<h1>Hello {{ user }}!</h1>
{% else %}
<h1>Hello stranger!</h1>
{% endif %}
#for循环
<ul>
    {% for comment in comment%}
        <li>{{comment}}</li>
    {% endfor %}
</ul>
# 宏（类似python）
{% macro render_comment(comment)%}
    <li>{{comment}}</li>
{% endmacro%}

<ul>
    {%for comment in comment%}
        {{render_comment(comment)}}
    {%endfor%}
</ul>