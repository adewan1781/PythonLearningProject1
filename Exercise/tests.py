from Exercise.BoxApplication import BoxApplication

if __name__ == "__main__":
    obj = BoxApplication()
    obj.open_browser()
    obj.login_box()
    obj.create_folder()
    obj.logout_box()
    obj.close_browser()
