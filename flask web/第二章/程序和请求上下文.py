
# 为了避免参数把程序弄乱，flask使用上下文临时把某些对象变成全局可访问
# 在分发请求之前激活程序和请求上下文，请求处理完成后再将其删除。程序上下文被推送后，
# 就可以在线程中使用current_app和g变量

from hello import app  #从hello文件导入app实例
from flask import current_app  #从flask包导入current_app对象
app_ctx=app.app_context()   #获得一个程序上下文（激活程序上下文），实际上是创建了一个AppContext类的实例
app_ctx.push()  #把程序上下文压入堆栈中
current_app.name
'hello' #当前激活程序的程序实例的名字
app_ctx.pop()#把上下文弹出








