import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from assets.styles import apply_global_styles
from ui.components.login_header import LoginHeader
from ui.components.auth_choice_button import AuthChoiceButtons
from ui.components.auth_form import AuthForm

apply_global_styles()

LoginHeader().render()
AuthChoiceButtons().render()
AuthForm().render()