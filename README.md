# Заметки Evernote

С помощью данного набора скриптов можно получить список блокнотов, заметки из блокнота, а также добавить новую заметку с определённой датой в заголовке.

### Как установить

Для использования скриптов нужна учётная запись [Evernote](https://sandbox.evernote.com/), и [токен](https://dev.evernote.com/key.php#) (ключ) для доступа к его API.
Также потребуется поместить следующие переменные окружения в файл **.env**:

| Переменная            | Описание |
| ------------ | ------------------- |
| EVERNOTE_CONSUMER_KEY<br>EVERNOTE_CONSUMER_SECRET<br>EVERNOTE_PERSONAL_TOKEN | Ключ пользователя, зашифрованный пароль и токен.<br>(Взять со страницы получения токена) |
| JOURNAL_TEMPLATE_NOTE_GUID | Идентификатор шаблона заметки |
| JOURNAL_NOTEBOOK_GUID | Идентификатор блокнота для добавления заметок |
| INBOX_NOTEBOOK_GUID | Идентификатор блокнота, заметки из которого нужно показать |

Файл нужно сохранить в каталоге со скриптами.

Пример файла:

```bash
EVERNOTE_CONSUMER_KEY='user_name'
EVERNOTE_CONSUMER_SECRET='7539fb3c725349ba'
EVERNOTE_PERSONAL_TOKEN='S=s1:U=9687f:E=19827615490:C=21c3d762601:P=1ba:A=en-devtoken:V=2:H=2c83d52e673b1064183a458b107de73c'
JOURNAL_TEMPLATE_NOTE_GUID='7c1e6183-2ba1-7613-bc59-c692b1941848'
JOURNAL_NOTEBOOK_GUID='7ae76731-aac8-94bd-c731-1a94173195b3'
INBOX_NOTEBOOK_GUID='72bfcd59-1a9e-73e3-c2b6-1a83de952173'
```

Python2 должен быть уже установлен. 
Затем используйте `pip` для установки зависимостей:

```
pip install -r requirements.txt
```

### Использование скриптов

- Скрипт **list_notebooks.py** выводит список блокнотов: 

	```bash
	python list_notebooks.py                
	7ae76731-aac8-94bd-c731-1a94173195b3 - Notebook1 name
	72bfcd59-1a9e-73e3-c2b6-1a83de952173 - Notebook2 name
	...
	```
	
- Скрипт **dump_inbox.py** выводит содержимое блокнота:

  ```
  python dump_inbox.py
  
  --------- 1 ---------
  
  Note text
  ...
  ```

- Скрипт add_note2journal.py добавляет новую заметку.

  В качестве аргумента можно указать дату в формате ГГГГ-ММ-ДД. При этом указанная дата и день недели появятся в заголовке добавленной заметки вместо {date} и {dow} в заголовке шаблона.

  Пример запуска:

  ```
  python add_note2journal.py 2021-11-26
  Title Context is:
  {
      "date": "2021-11-26",
      "dow": "пятница"
  }
  Note created: пятница - 2021-11-26
  Done
  ```



### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).