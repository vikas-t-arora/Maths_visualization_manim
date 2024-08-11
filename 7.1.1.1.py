from manimlib.imports import *

#from big_ol_pile_of_manim_imports import *

def set_background(self):
    background = Rectangle(
    width = FRAME_WIDTH,
    height = FRAME_HEIGHT,
    stroke_width = 0,
    fill_color = "#1F899F",
    fill_opacity = 1)
    self.add(background)


a=3
b=np.sqrt(a)
class CreateTraiangle(Scene):
    def construct(self):
        triangle=Polygon(np.array([a/2,a/(2*b),0]),np.array([-a/2,a/(2*b),0]),np.array([0,-a/b,0]))
        triangle1=Polygon(np.array([0,a/(2*b),0]),np.array([-a/2,a/(2*b),0]),np.array([-a/4,-a/(4*b),0]))
        triangle2=Polygon(np.array([0,a/(2*b),0]),np.array([-a/4,-a/(4*b),0]),np.array([a/4,-a/(4*b),0]))
        triangle3=Polygon(np.array([a/2,a/(2*b),0]),np.array([0,a/(2*b),0]),np.array([a/4,-a/(4*b),0]))
        triangle4=Polygon(np.array([a/4,-a/(4*b),0]),np.array([-a/4,-a/(4*b),0]),np.array([0,-a/b,0]))
        triangle3.set_fill(BLUE,opacity=0.5)
        triangle4.set_fill(BLUE,opacity=0.5)
        #set_background(self)
        self.play(ShowCreation(triangle1),ShowCreation(triangle2),ShowCreation(triangle3),ShowCreation(triangle4),ShowCreation(triangle))
        self.wait(1)
        self.play(FadeOut(triangle),ApplyMethod(triangle1.shift,2*LEFT+2*UP),ApplyMethod(triangle2.shift,3*LEFT+2*DOWN),ApplyMethod(triangle3.shift,2*RIGHT+2*UP),ApplyMethod(triangle4.shift,3*RIGHT+1*DOWN))
        self.wait(1)
        self.play(ApplyMethod(triangle2.shift,0.25*RIGHT+4*UP))
        self.play(ApplyMethod(triangle2.flip, LEFT))
        self.wait(1)
        self.play(ApplyMethod(triangle2.flip, LEFT))
        self.play(ApplyMethod(triangle2.shift,0.25*LEFT+4*DOWN))
        self.play(ApplyMethod(triangle3.shift,5.5*LEFT))
        self.wait(1)
        self.play(ApplyMethod(triangle3.shift,5.5*RIGHT))
        self.play(ApplyMethod(triangle4.shift,5.75*LEFT+4.3*UP))
        self.wait(1)
        self.play(ApplyMethod(triangle4.shift,5.75*RIGHT+4.3*DOWN))
        self.wait(1)
        txt=TextMobject("The number of filled small triangles =").next_to(triangle,9*UP)
        self.play(ShowCreation(txt))
        self.wait(1)
        txt5=TextMobject("1",color=GREEN).shift(2.7*RIGHT+2.3*UP)
        self.play(ShowCreation(txt5))
        txt6=TextMobject("2",color=GREEN).shift(3*RIGHT+2*DOWN)
        self.play(ShowCreation(txt6))
        self.play(FadeOut(txt5),ApplyMethod(txt6.shift,2*RIGHT+5.4*UP))
        self.wait(1)
        txtt=TextMobject("The total number of small triangles =").next_to(triangle,5*DOWN)
        self.play(ShowCreation(txtt))
        txt1=TextMobject("1",color=RED).shift(2.75*LEFT+2.4*UP)
        self.play(ShowCreation(txt1))
        txt2=TextMobject("2",color=RED).shift(3*LEFT+2*DOWN)
        self.play(ShowCreation(txt2))
        txt3=TextMobject("3",color=RED).shift(2.7*RIGHT+2.3*UP)
        self.play(ShowCreation(txt3))
        txt4=TextMobject("4",color=RED).shift(3*RIGHT+2*DOWN)
        self.play(ShowCreation(txt4))
        self.play(FadeOut(txt1),FadeOut(txt2),FadeOut(txt3),ApplyMethod(txt4.shift,2*RIGHT+1.22*DOWN))
        self.wait(1)
        self.play(FadeIn(triangle),ApplyMethod(triangle1.shift,2*RIGHT+2*DOWN),ApplyMethod(triangle2.shift,3*RIGHT+2*UP),ApplyMethod(triangle3.shift,2*LEFT+2*DOWN),ApplyMethod(triangle4.shift,3*LEFT+1*UP))
        self.wait(1)
        txt7=TextMobject("Fraction = ------ = ---").next_to(triangle)
        self.play(ShowCreation(txt7))
        self.play(FadeOut(txt),FadeOut(txtt),ApplyMethod(txt6.shift,0.25*LEFT+3.55*DOWN),ApplyMethod(txt4.shift,0.25*LEFT+2.4*UP))
        self.wait(1)
        txt8=TextMobject("2*1",color=GREEN).shift(4.75*RIGHT+0.1*DOWN)
        txt9=TextMobject("2*2",color=RED).shift(4.75*RIGHT+0.9*DOWN)
        self.play(Transform(txt6,txt8),Transform(txt4,txt9))
        self.wait(1)
        txt10=TextMobject("/").shift(4.5*RIGHT+0.1*DOWN)
        txt11=TextMobject("/").shift(4.5*RIGHT+0.9*DOWN)
        self.play(ShowCreation(txt10),ShowCreation(txt11))
        self.wait(1)
        txt12=TextMobject("1",color=GREEN).shift(6.25*RIGHT+0.1*DOWN)
        txt13=TextMobject("2",color=RED).shift(6.25*RIGHT+0.9*DOWN)
        self.play(ShowCreation(txt12),ShowCreation(txt13))
        self.wait(2)

        

#class CreateSquare(Scene):
#    def construct(self):
#       sqr = Square(side_length = 2)
#        self.play(ShowCreation(sqr))
#        self.wait(2)