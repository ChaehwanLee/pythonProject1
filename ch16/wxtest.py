# wxtest

import wx;

app = wx.App();
frame = wx.Frame(None, 0, 'Test');

p1 = wx.Panel(frame);
bt1 = wx.Button(p1,label='Button1');
bt2 = wx.Button(p1,label='Button2');
bt3 = wx.Button(p1,label='Button3');

ps = wx.BoxSizer(wx.HORIZONTAL);
ps.Add(bt1);
ps.Add(bt2);
ps.Add(bt3);
p1.SetSizer(ps);

p2 = wx.Panel(frame);
text1 = wx.StaticText(p2,label='                a               ');
text2 = wx.StaticText(p2,label='                b               ');
text3 = wx.StaticText(p2,label='                v               ');
ps2 = wx.BoxSizer(wx.VERTICAL);
ps2.Add(text1);
ps2.Add(text2);
ps2.Add(text3);
p2.SetSizer(ps2);

p2 = wx.Panel(frame);
names = ['abc','ed','fse','gfse']
list = wx.ListBox(p2, choices= names);
list.SetSize(wx.Size(300,200))

box = wx.BoxSizer(wx.VERTICAL);
frame.SetSizer(box);
box.Add(p1,border=10,flag=wx.DOWN);
box.Add(p2,border=10,flag=wx.UP);

# def clickbt1(event):
#     text1.SetLabelText('Click button 1');
# def clickbt2(event):
#     text1.SetLabelText('Click button 2');
# def clickbt3(event):
#     text1.SetLabelText('Click button 3');

def clickbtn1(event):
    list.Clear();
    items = ['111', '222', '333', '444'];
    list.Append(items);
def clickbtn2(event):
    list.Clear();
    items = ['555', '666', '777', '888'];
    list.Append(items);
def clickbtn3(event):
    list.Clear();
    items = ['999', '000', '111', '222'];
    list.Append(items);

bt1.Bind(wx.EVT_BUTTON, clickbtn1);
bt2.Bind(wx.EVT_BUTTON, clickbtn2);
bt3.Bind(wx.EVT_BUTTON, clickbtn3);

frame.Show(True);
app.MainLoop();