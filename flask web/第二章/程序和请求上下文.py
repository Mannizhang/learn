from flask import Flask

app = Flask(__name__)

# 为了避免参数把程序弄乱，flask使用上下文临时把某些对象变成全局可访问
# 在分发请求之前激活程序和请求上下文，请求处理完成后再将其删除。程序上下文被推送后，
# 就可以在线程中使用current_app和g变量










