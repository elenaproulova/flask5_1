from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на свой секретный ключ

class EditProfileForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=30)])
    email = EmailField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Сохранить изменения')

@app.route('/')
def home():
    return redirect(url_for('edit_profile'))

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Здесь вы можете обработать сохранение данных в базе данных
        # Например, обновить пользователя в базе данных
        flash('Профиль успешно обновлён!', 'success')
        return redirect(url_for('edit_profile'))
    return render_template('edit_profile.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)