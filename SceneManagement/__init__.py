
class SceneManager:
    def __init__(self):
        self.sceneDict = {}
        self.activeScene = None

    def click(self, pos):
        assert self.activeScene is not None
        self.activeScene.click(pos)

    def update(self):
        assert self.activeScene is not None
        self.activeScene.update()

    def draw(self, canvas):
        assert self.activeScene is not None
        self.activeScene.draw(canvas)

    def updateScene(self, sceneName):
        #if scene object was given
        if sceneName in self.sceneDict.values():
            self.activeScene = sceneName
            self.activeScene.load()
            return

        #if key was given
        if sceneName in self.sceneDict:
            self.activeScene = self.sceneDict[sceneName]
            self.activeScene.load()
            return

        assert False

    def registerScene(self, scene):
        self.sceneDict[scene.name] = scene
        scene.manager = self

class Scene:
    def __init__(self, manager):
        self.name = None
        self.manager = None

    def load(self):
        pass

    def unload(self):
        pass

    def draw(self, canvas):
        pass

    def update(self):
        pass

    def click(self, pos):
        pass

    def __repr__(self):
        return "Scene: \"%s\"" % self.name

def __test():
    class A(Scene):
        def __init__(self, manager):
            Scene.__init__(self, manager)
            self.name = "a"

        def click(self, pos):
            self.manager.updateScene("b")

    class B(Scene):
        def __init__(self, manager):
            Scene.__init__(self, manager)
            self.name = "b"

        def click(self, pos):
            self.manager.updateScene("a")

    mgr = SceneManager()
    a = A(mgr)
    b = B(mgr)
    mgr.registerScene(a)
    mgr.registerScene(b)
    mgr.updateScene("a")
    print mgr.activeScene
    mgr.click(None)
    print mgr.activeScene
    mgr.click(None)
    print mgr.activeScene
    mgr.click(None)
    print mgr.activeScene

if __name__ == '__main__':
    __test()

