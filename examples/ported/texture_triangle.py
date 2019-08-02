import numpy as np
from PIL import Image

import _simple_2d_example


class Example(_simple_2d_example.Example):
    title = 'Texture Triangle'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # the shader program is inherited
        # self.prog = self.ctx.program(...)
        self.prog['RenderMode'].value = self.TEXTURE_MODE

        vertices = np.array([
            # x, y, tx, ty
            0.0, 0.8, 0.5, 1.0,
            -0.6, -0.8, 0.0, 0.0,
            0.6, -0.8, 1.0, 0.0,
        ])

        img = Image.open('examples/data/wood.jpg')
        texture = self.ctx.texture(img.size, 3, img.tobytes())
        texture.use()

        self.vbo = self.ctx.buffer(vertices.astype('f4').tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_text')

    def render(self, time: float, frame_time: float):
        self.ctx.clear(1.0, 1.0, 1.0)
        self.vao.render()


if __name__ == '__main__':
    Example.run()
