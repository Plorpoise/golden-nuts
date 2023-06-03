import pytest
import GUIView

#darkmode test
def test_darkmode(view: GUIView):
    view.set_darkmode(True)
    assert view.bg_color == GUIView.Color.BLACK
    assert view.text_color == GUIView.Color.WHITE
    assert view.border_color == GUIView.Color.BLACK
    assert view.graph_bg_color == GUIView.Color.GREY

#lightmode test
def test_lightmode(view: GUIView):
    view.set_darkmode(False)
    assert view.bg_color == GUIView.Color.WHITE
    assert view.text_color == GUIView.Color.BLACK
    assert view.border_color == GUIView.Color.BLACK
    assert view.graph_bg_color == GUIView.Color.WHITE

