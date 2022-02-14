# wxtest2

import wx;
import weather;
import itemdb;

app = wx.App();
frame = wx.Frame(None, 0, 'Test');

p1 = wx.Panel(frame);
bt1 = wx.Button(p1, label='Button1');
bt2 = wx.Button(p1, label='Button2');
bt3 = wx.Button(p1, label='Button3');
ps = wx.BoxSizer(wx.HORIZONTAL);
ps.Add(bt1);
ps.Add(bt2);
ps.Add(bt3);
p1.SetSizer(ps);

p2 = wx.Panel(frame);
names = ['abc', 'eds', 'fse', 'gfsd'];
list = wx.ListBox(p2, choices=names);
list.SetSize(wx.Size(300, 200));

p3 = wx.Panel(frame); #패널
bt_add = wx.Button(p3, label='ADD'); #버튼
text1 = wx.TextCtrl(p3); #텍스트
text2 = wx.TextCtrl(p3);
text3 = wx.TextCtrl(p3);
text4 = wx.TextCtrl(p3);
ps3 = wx.BoxSizer(wx.VERTICAL); #박스
ps3.Add(bt_add);
ps3.Add(text1);
ps3.Add(text2);
ps3.Add(text3);
ps3.Add(text4);
p3.SetSizer(ps3);

def clickadd(event): # 버튼이 눌리는 순간 값을 가져와라
    id = int(text1.GetValue());
    name = text2.GetValue();
    price = int(text3.GetValue());
    rate = float(text4.GetValue());
    try:
        itemdb.insert(id, name, price, rate);
        text1.SetLabelText('');
        text2.SetLabelText('');
        text3.SetLabelText('');
        text4.SetLabelText('');
    except:
        wx.MessageBox('Insert Error', 'Alert',wx.OK); #화면에 출력을 해줘야한다
bt_add.Bind(wx.EVT_BUTTON, clickadd);

box = wx.BoxSizer(wx.VERTICAL);
frame.SetSizer(box);
box.Add(p1, border=10, flag=wx.DOWN);
box.Add(p2, border=10, flag=wx.UP);
box.Add(p3, border=10, flag=wx.UP); #Add 버튼

def clickbt1(event):
    list.Clear();
    items = weather.getdata();
    list.AppendItems(items);
def clickbt2(event):
    list.Clear();
    items = itemdb.selectui();
    list.AppendItems(items);
def clickbt3(event):
    list.Clear();
    items = ['999', '000', '111', '222'];
    list.AppendItems(items);
bt1.Bind(wx.EVT_BUTTON, clickbt1);
bt2.Bind(wx.EVT_BUTTON, clickbt2);
bt3.Bind(wx.EVT_BUTTON, clickbt3);

frame.Show(True);
app.MainLoop();