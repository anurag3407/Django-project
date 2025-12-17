# 🐦 Twitter Clone - Django Social Media Application

A fully-featured Twitter clone built with Django and styled with Tailwind CSS. This application allows users to create, read, update, and delete tweets, search for content, and interact with a beautiful, modern UI.

![Twitter Clone](https://img.shields.io/badge/Django-6.0-green)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38bdf8)

## ✨ Features

### Core Functionality
- 🔐 **User Authentication**: Complete registration and login system
- 📝 **Tweet Creation**: Post tweets up to 280 characters with optional photos
- ✏️ **Tweet Editing**: Edit your own tweets anytime
- 🗑️ **Tweet Deletion**: Remove tweets you've posted
- 🔍 **Search Feature**: Search tweets by content or username
- 📱 **Responsive Design**: Mobile-friendly interface that works on all devices

### User Interface
- 🎨 **Modern UI**: Polished interface with Tailwind CSS
- 🌈 **Gradient Effects**: Beautiful color gradients and hover effects
- ✨ **Smooth Animations**: Transitions and transform effects
- 🖼️ **Image Support**: Upload and display photos with tweets
- 💬 **Interactive Elements**: Hoverable buttons with visual feedback
- 📊 **Clean Typography**: Easy-to-read fonts and spacing

### Additional Features
- ⏰ **Timestamps**: See when tweets were posted with relative time
- 👤 **User Profiles**: Avatar initials for each user
- 🏠 **Home Page**: Quick access to latest tweets and actions
- 📋 **Tweet Feed**: View all tweets in chronological order
- 🔎 **Advanced Search**: Filter by content and usernames

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning)

### Installation

1. **Clone the repository** (or download the ZIP file)
   ```bash
   git clone https://github.com/anurag3407/Django-project.git
   cd Django-project/twitter
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (admin account)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up your admin username, email, and password.

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to:
   - Main site: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📖 Usage Guide

### Creating an Account
1. Click on **"Sign Up"** in the navigation bar
2. Fill in your username, email, and password
3. Submit the form to create your account
4. You'll be automatically logged in

### Posting a Tweet
1. Click on **"Create Tweet"** or the **"Tweet"** button
2. Enter your message (up to 280 characters)
3. Optionally, upload a photo
4. Click **"Post Tweet"** to publish

### Searching for Tweets
1. Use the search bar in the navigation (desktop)
2. Or click **"Search"** in the menu
3. Enter keywords or usernames
4. View matching results instantly

### Managing Your Tweets
- **Edit**: Click the blue edit icon on your tweets
- **Delete**: Click the red delete icon and confirm
- Only you can edit or delete your own tweets

### Exploring Content
- **Home**: View latest 5 tweets and quick actions
- **All Tweets**: Browse all tweets from all users
- **Search**: Find specific tweets or users

## 🏗️ Project Structure

```
twitter/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── README.md                # This file
├── static/                  # Static files (media uploads)
├── tweet/                   # Main app
│   ├── models.py           # Tweet model definition
│   ├── views.py            # View functions (logic)
│   ├── forms.py            # Form definitions
│   ├── urls.py             # App URL patterns
│   ├── admin.py            # Admin configuration
│   ├── migrations/         # Database migrations
│   └── templates/          # HTML templates
│       ├── index.html
│       ├── tweet_list.html
│       ├── tweet_form.html
│       ├── tweet_search.html
│       └── tweet_confirm_delete.html
└── twitter/                 # Project settings
    ├── settings.py         # Django settings
    ├── urls.py             # Main URL configuration
    ├── wsgi.py             # WSGI config
    └── templates/          # Base templates
        ├── layout.html     # Base layout with navbar
        ├── login.html
        └── register.html
```

## 🛠️ Technology Stack

### Backend
- **Django 6.0**: High-level Python web framework
- **SQLite**: Lightweight database (default)
- **Pillow**: Python Imaging Library for photo uploads

### Frontend
- **HTML5**: Markup structure
- **Tailwind CSS**: Utility-first CSS framework (via CDN)
- **JavaScript**: Interactive elements and form validation

### Key Django Features Used
- Django ORM (Object-Relational Mapping)
- Class-based and function-based views
- Django Forms and ModelForms
- User authentication system
- Template inheritance
- Static files management
- URL routing

## 📝 Models

### Tweet Model
```python
class Tweet(models.Model):
    user = ForeignKey(User)           # Tweet author
    content = CharField(max_length=280) # Tweet text
    photo = ImageField(optional)       # Optional image
    created_at = DateTimeField         # Creation timestamp
    updated_at = DateTimeField         # Last update timestamp
```

## 🔒 Security Features

- CSRF protection on all forms
- User authentication required for tweet creation/editing
- User authorization (can only edit/delete own tweets)
- Secure password hashing
- SQL injection prevention (Django ORM)

## 🎨 UI/UX Highlights

- **Gradient Backgrounds**: Eye-catching blue and purple gradients
- **Hover Effects**: Interactive buttons with scale and color transitions
- **Smooth Animations**: Transform effects on cards and buttons
- **Responsive Grid**: Adapts to mobile, tablet, and desktop
- **Visual Feedback**: Hover states on all interactive elements
- **Clean Cards**: Modern card design with shadows
- **Icon Integration**: SVG icons for actions (edit, delete, like, etc.)

## 🚀 Deployment Tips

For production deployment, consider:

1. **Security Settings**
   ```python
   DEBUG = False
   SECRET_KEY = os.environ.get('SECRET_KEY')
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

2. **Database**: Upgrade to PostgreSQL or MySQL
3. **Static Files**: Use WhiteNoise or cloud storage
4. **Media Files**: Use AWS S3 or similar
5. **Environment Variables**: Use python-deotenv
6. **HTTPS**: Configure SSL certificates
7. **Hosting**: Deploy on Heroku, Railway, PythonAnywhere, or DigitalOcean

## 🐛 Troubleshooting

### Common Issues

**Issue**: Cannot upload images
- **Solution**: Make sure Pillow is installed: `pip install pillow`
- Check MEDIA_ROOT and MEDIA_URL settings

**Issue**: Static files not loading
- **Solution**: Run `python manage.py collectstatic`
- Ensure DEBUG=True for development

**Issue**: Database errors
- **Solution**: Delete `db.sqlite3` and run migrations again:
  ```bash
  python manage.py migrate
  ```

**Issue**: Port already in use
- **Solution**: Use a different port:
  ```bash
  python manage.py runserver 8080
  ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📋 Future Enhancements

Potential features to add:
- [ ] Like and retweet functionality
- [ ] User profiles with bio and profile pictures
- [ ] Follow/unfollow users
- [ ] Comment on tweets
- [ ] Real-time notifications
- [ ] Hashtag support
- [ ] Trending topics
- [ ] Direct messaging
- [ ] Email verification
- [ ] Password reset functionality
- [ ] Tweet analytics
- [ ] Dark mode toggle

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Anurag**
- GitHub: [@anurag3407](https://github.com/anurag3407)

## 🙏 Acknowledgments

- Django documentation and community
- Tailwind CSS for the amazing utility classes
- Heroicons for the beautiful SVG icons
- All contributors and users of this project

## 📞 Support

If you have any questions or issues, please:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an issue on GitHub
3. Contact the maintainer

---

**Happy Tweeting! 🐦✨**

Made with ❤️ using Django and Tailwind CSS
