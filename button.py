import pygame.font,tkinter,time

class Button():
    def __init__(self, screen, msg, c1, c2, c3, px, py, rx = 100, ry = 50, fontsize=32):
        self.screen = screen
        self.screen_rect=screen.get_rect()  
        self.width,self.height=rx, ry  #這種賦值方式很不錯
        self.button_color=(c1,c2,c3)  #設定按鈕的rect物件顏色為深藍
        self.text_color=(0,0,0)  #設定文字的顏色為白色
        self.font=pygame.font.Font('Font\\新篆體.TTC',fontsize)     #設定文字為預設字型，字號為40
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=(px,py)   #建立按鈕的rect物件，並使其居中
        self.deal_msg(msg, px,py)  #渲染影象

    def deal_msg(self,msg, px, py):       
        """將msg渲染為影象，並將其在按鈕上居中"""
        self.msg_img=self.font.render(msg,True,self.text_color,self.button_color) #render將儲存在msg的文字轉換為影象
        self.msg_img_rect=self.msg_img.get_rect()  #根據文字影象建立一個rect
        self.msg_img_rect.center=(px,py)  #將該rect的center屬性設定為按鈕的center屬性
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)  #填充顏色
        self.screen.blit(self.msg_img,self.msg_img_rect) #將該影象繪製到螢幕