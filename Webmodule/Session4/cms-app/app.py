
from designe.video import Video
import mlab
from youtube_dl import YoutubeDL
from flask import *

mlab.connect()
app = Flask(__name__)
#session required a sercret key
app.secret_key = "A super sercet key"



@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos= videos)

@app.route('/admin', methods = ["GET", "POST"])
def admin():
    if "loggedin" in session:
        if request.method == "GET":
            videos = Video.objects()
            return render_template ("admin.html", videos =videos)
        elif request.method == "POST":
            form = request.form
            link = form['Link']
            ydl = YoutubeDL()
            # Ham extract info
            data = ydl.extract_info(link, download= False)


            title = data['title']
            thumbnail = data['thumbnail']
            views = data['view_count']
            youtube_id = data['id']


            video = Video(  title= title,
                            thumbnail= thumbnail,
                            view= views,
                            youtube_id=youtube_id,
                            link=link)

            video.save()

            return redirect(url_for("admin"))
    else:
        return redirect(url_for("login"))

@app.route('/delete/<video_id>')
def delete(video_id):
    video_to_delete = Video.objects.with_id(video_id)
    # Video là tên collection
    if video_to_delete is not None:
        video_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Video not found"

@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template("detail.html", youtube_id=youtube_id)
@app.route ('/login', methods= ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for('admin'))
        else:
            return "Permission denied. Go away!!"

@app.route ('/logout')
def logout():
    if 'loggedin' in session:
        del session['loggedin']
        return redirect(url_for('admin'))
    else:
        print("You haven't login yet")
        return redirect(url_for('admin'))


if __name__ == '__main__':
  app.run( debug=True)
