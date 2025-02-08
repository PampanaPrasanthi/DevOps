from flask import Flask, request, render_template
app = Flask( name )
@app.route(&#39;/&#39;)
def home():
return &quot;welcome to the Flask App1go to /register&quot;
@app.route(&#39;/register&#39;, methods=[&#39;GET&#39;, &#39;POST&#39;])
def register():
if request.method == &#39;POST&#39;:
name = request.form[&#39;name&#39;]
email = request.form[&#39;email&#39;]
password = request.form[&#39;password&#39;]
return render_template(&#39;Success.html&#39;, name=name, email=email)

return render_template(&#39;Register.html&#39;)
if name == &#39; main &#39;:
app.run(debug=True)
