from tkinter import *
import speedtest


#спид тест для проверки скорости
def test():
    download = speedtest().download()
    upload = speedtest().upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    download_label.config(text = 'Скорость закрузки:\n-' + str(download_speed) + 'MbPs')
    upload_label.config(text = 'Скорость отдачи:\n-' + str(upload_speed) + 'MbPs')

#ВНИЗУ КАРКАС
root = Tk()

root.title('SpeedTest')
root.geometry('300x400')

#САМАЯ НИЖНЯЯ КНОПКА
button = Button(root , text = 'Жми сюда' , font = 40, command = test)
button.pack(side = BOTTOM , pady = 40)


Download_label = Label(root , text='Скорость закрузки:\n-' , font = 35)
Download_label.pack(pady = (50 , 0))

upload_label = Label(root , text = 'Скорость отдачи:\n-' , font = 35)
upload_label.pack(pady = (10 , 0))

 #ВЫВОД
root.mainloop()