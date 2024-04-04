from flask import Flask
from views import views
app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")
if __name__ == '__main__':
    app.run(debug=True)

    @views.route("/profile")
    def profile():
        return render_templates("index.html", name=name)

lottie_coding = "https://lottiefiles.com/animations/phone-call-Mn4d2NpZDo"


st.set_page_config(page_title="Lets Grow Together", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
st.subheader("Hi, We are so exicted you are here :wave:")

st.title("Let Us Make The Calls")

st.write("Our team makes hundreds of cold calls per day. We strive to provide as many new leads for your businesses as possible. Simply provide the zip code in which you are trying to grow and we will take it from there. When you grow, we grow. So lets grow together.")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We Do")
        st.write("We resarch the zip code in which you provide, and identify a list of businesses that potentially could use your product or services. Once we have this list established we send this list to you for approval. After you approve the list, we start out calling and advertising your business.")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
