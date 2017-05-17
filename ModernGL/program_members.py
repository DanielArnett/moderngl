'''
    ModernGL program members
'''

# pylint: disable=too-few-public-methods


class Uniform:
    '''
        Uniform
    '''

    def __init__(self):
        self.mglo = None
        raise NotImplementedError('Uniform')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = Uniform.__new__(Uniform)
        res.mglo = obj
        return res

    @property
    def name(self) -> str:
        '''
            The name of the uniform.
            The name does not contain leading `[0]`.
            The name may contain `[ ]` when the uniform is part of a struct.

            :type: str
        '''

        return self.mglo.name

    @property
    def location(self) -> int:
        '''
            The location of the uniform.

            :type: int
        '''

        return self.mglo.location

    @property
    def dimension(self) -> int:
        '''
            The dimension of the uniform.

            +-----------------+-----------+
            | GLSL type       | dimension |
            +=================+===========+
            | sampler2D       | 1         |
            +-----------------+-----------+
            | sampler2DCube   | 1         |
            +-----------------+-----------+
            | sampler2DShadow | 1         |
            +-----------------+-----------+
            | bool            | 1         |
            +-----------------+-----------+
            | bvec2           | 2         |
            +-----------------+-----------+
            | bvec3           | 3         |
            +-----------------+-----------+
            | bvec4           | 4         |
            +-----------------+-----------+
            | int             | 1         |
            +-----------------+-----------+
            | ivec2           | 2         |
            +-----------------+-----------+
            | ivec3           | 3         |
            +-----------------+-----------+
            | ivec4           | 4         |
            +-----------------+-----------+
            | uint            | 1         |
            +-----------------+-----------+
            | uvec2           | 2         |
            +-----------------+-----------+
            | uvec3           | 3         |
            +-----------------+-----------+
            | uvec4           | 4         |
            +-----------------+-----------+
            | float           | 1         |
            +-----------------+-----------+
            | vec2            | 2         |
            +-----------------+-----------+
            | vec3            | 3         |
            +-----------------+-----------+
            | vec4            | 4         |
            +-----------------+-----------+
            | double          | 1         |
            +-----------------+-----------+
            | dvec2           | 2         |
            +-----------------+-----------+
            | dvec3           | 3         |
            +-----------------+-----------+
            | dvec4           | 4         |
            +-----------------+-----------+
            | mat2            | 4         |
            +-----------------+-----------+
            | mat2x3          | 6         |
            +-----------------+-----------+
            | mat2x4          | 8         |
            +-----------------+-----------+
            | mat3x2          | 6         |
            +-----------------+-----------+
            | mat3            | 9         |
            +-----------------+-----------+
            | mat3x4          | 12        |
            +-----------------+-----------+
            | mat4x2          | 8         |
            +-----------------+-----------+
            | mat4x3          | 12        |
            +-----------------+-----------+
            | mat4            | 16        |
            +-----------------+-----------+
            | dmat2           | 4         |
            +-----------------+-----------+
            | dmat2x3         | 6         |
            +-----------------+-----------+
            | dmat2x4         | 8         |
            +-----------------+-----------+
            | dmat3x2         | 6         |
            +-----------------+-----------+
            | dmat3           | 9         |
            +-----------------+-----------+
            | dmat3x4         | 12        |
            +-----------------+-----------+
            | dmat4x2         | 8         |
            +-----------------+-----------+
            | dmat4x3         | 12        |
            +-----------------+-----------+
            | dmat4           | 16        |
            +-----------------+-----------+

            :type: int
        '''

        return self.mglo.dimension

    @property
    def array_length(self) -> int:
        '''
            The length of the array of the uniform.
            The array_length is `1` for non array uniforms.

            :type: int
        '''

        return self.mglo.array_length

    @property
    def value(self):
        '''
            The value of the uniform.
            Reading the value of the uniform may force the GPU to sync.

            The value must be a tuple for non array uniforms.
            The value must be a list of tuples for array uniforms.
        '''

        return self.mglo.value

    @value.setter
    def value(self, value):
        self.mglo.value = value


class UniformMap:
    '''
        UniformMap
    '''

    def __init__(self):
        self.mglo = {}
        raise NotImplementedError('UniformMap')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = UniformMap.__new__(UniformMap)
        res.mglo = obj
        return res

    def __getitem__(self, key) -> Uniform:
        '''
        '''

        return Uniform.new(self.mglo[key])

    def __contains__(self, key):
        return key in self.mglo

    def __len__(self):
        return len(self.mglo)


class UniformBlock:
    '''
        UniformBlock
    '''

    def __init__(self):
        self.mglo = None
        raise NotImplementedError('UniformBlock')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = UniformBlock.__new__(UniformBlock)
        res.mglo = obj
        return res

    @property
    def name(self):
        '''
            name
        '''

        return self.mglo.name

    @property
    def location(self):
        '''
            location
        '''

        return self.mglo.location


class UniformBlockMap:
    '''
        UniformBlockMap
    '''

    def __init__(self):
        self.mglo = {}
        raise NotImplementedError('UniformBlockMap')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = UniformBlockMap.__new__(UniformBlockMap)
        res.mglo = obj
        return res

    def __getitem__(self, key) -> UniformBlock:
        '''
        '''

        return UniformBlock.new(self.mglo[key])

    def __contains__(self, key):
        return key in self.mglo

    def __len__(self):
        return len(self.mglo)


class Varying:
    '''
        Varying
    '''

    def __init__(self):
        self.mglo = None
        raise NotImplementedError('Varying')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = Varying.__new__(Varying)
        res.mglo = obj
        return res

    @property
    def name(self):
        '''
            name
        '''

        return self.mglo.name

    @property
    def number(self):
        '''
            number
        '''

        return self.mglo.number


class VaryingMap:
    '''
        VaryingMap
    '''

    def __init__(self):
        self.mglo = {}
        raise NotImplementedError('VaryingMap')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = VaryingMap.__new__(VaryingMap)
        res.mglo = obj
        return res

    def __getitem__(self, key) -> Varying:
        '''
        '''

        return Varying.new(self.mglo[key])

    def __contains__(self, key):
        return key in self.mglo

    def __len__(self):
        return len(self.mglo)


class Attribute:
    '''
        Attribute
    '''

    def __init__(self):
        self.mglo = None
        raise NotImplementedError('Attribute')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = Attribute.__new__(Attribute)
        res.mglo = obj
        return res

    @property
    def name(self):
        '''
            The attribute name.
            The name will be filtered to have no array syntax on it's end.
            Attribute name without ``'[0]'`` ending if any.
        '''

        return self.mglo.name

    @property
    def location(self):
        '''
            The attribute location.
            The result of the glGetAttribLocation.
        '''

        return self.mglo.location

    @property
    def array_length(self):
        '''
            If the attribute is an array the array_length is the length of the array otherwise `1`.
        '''

        return self.mglo.array_length

    @property
    def dimension(self):
        '''
            The attribute dimension.

            +-----------+-----------+
            | GLSL type | dimension |
            +===========+===========+
            | int       | 1         |
            +-----------+-----------+
            | ivec2     | 2         |
            +-----------+-----------+
            | ivec3     | 3         |
            +-----------+-----------+
            | ivec4     | 4         |
            +-----------+-----------+
            | uint      | 1         |
            +-----------+-----------+
            | uvec2     | 2         |
            +-----------+-----------+
            | uvec3     | 3         |
            +-----------+-----------+
            | uvec4     | 4         |
            +-----------+-----------+
            | float     | 1         |
            +-----------+-----------+
            | vec2      | 2         |
            +-----------+-----------+
            | vec3      | 3         |
            +-----------+-----------+
            | vec4      | 4         |
            +-----------+-----------+
            | double    | 1         |
            +-----------+-----------+
            | dvec2     | 2         |
            +-----------+-----------+
            | dvec3     | 3         |
            +-----------+-----------+
            | dvec4     | 4         |
            +-----------+-----------+
            | mat2      | 4         |
            +-----------+-----------+
            | mat2x3    | 6         |
            +-----------+-----------+
            | mat2x4    | 8         |
            +-----------+-----------+
            | mat3x2    | 6         |
            +-----------+-----------+
            | mat3      | 9         |
            +-----------+-----------+
            | mat3x4    | 12        |
            +-----------+-----------+
            | mat4x2    | 8         |
            +-----------+-----------+
            | mat4x3    | 12        |
            +-----------+-----------+
            | mat4      | 16        |
            +-----------+-----------+
            | dmat2     | 4         |
            +-----------+-----------+
            | dmat2x3   | 6         |
            +-----------+-----------+
            | dmat2x4   | 8         |
            +-----------+-----------+
            | dmat3x2   | 6         |
            +-----------+-----------+
            | dmat3     | 9         |
            +-----------+-----------+
            | dmat3x4   | 12        |
            +-----------+-----------+
            | dmat4x2   | 8         |
            +-----------+-----------+
            | dmat4x3   | 12        |
            +-----------+-----------+
            | dmat4     | 16        |
            +-----------+-----------+
        '''

        return self.mglo.dimension

    @property
    def shape(self):
        '''
            The shape is a single character, representing the scalar type of the attriute.

            +---------+--------------------------+
            | shape   | GLSL types               |
            +=========+==========================+
            | ``'i'`` | int                      |
            |         +--------------------------+
            |         | ivec2 ivec3 ivec4        |
            +---------+--------------------------+
            | ``'I'`` | uint                     |
            |         +--------------------------+
            |         | uvec2 uvec3 uvec4        |
            +---------+--------------------------+
            | ``'f'`` | float                    |
            |         +--------------------------+
            |         | vec2 vec3 vec4           |
            |         +--------------------------+
            |         | mat2 mat3 mat4           |
            |         +--------------------------+
            |         | mat2x3 mat2x4 mat3x4     |
            |         | mat4x2 mat4x2 mat4x3     |
            +---------+--------------------------+
            | ``'d'`` | double                   |
            |         +--------------------------+
            |         | dvec2 dvec3 dvec4        |
            |         +--------------------------+
            |         | dmat2 dmat3 dmat4        |
            |         +--------------------------+
            |         | dmat2x3 dmat2x4 dmat3x4  |
            |         | dmat4x2 dmat4x2 dmat4x3  |
            +---------+--------------------------+
        '''

        return self.mglo.shape


class AttributeMap:
    '''
        AttributeMap
    '''

    def __init__(self):
        self.mglo = {}
        raise NotImplementedError('AttributeMap')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = AttributeMap.__new__(AttributeMap)
        res.mglo = obj
        return res

    def __getitem__(self, key) -> Attribute:
        '''
        '''

        return Attribute.new(self.mglo[key])

    def __contains__(self, key):
        return key in self.mglo

    def __len__(self):
        return len(self.mglo)


class Subroutine:
    '''
        Subroutine
    '''

    def __init__(self):
        self.mglo = None
        raise NotImplementedError('Subroutine')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = Subroutine.__new__(Subroutine)
        res.mglo = obj
        return res

    @property
    def name(self):
        '''
            The name of the subroutine.
        '''

        return self.mglo.name

    @property
    def index(self):
        '''
            The index of the subroutine.
        '''

        return self.mglo.index


class SubroutineMap:
    '''
        SubroutineMap
    '''

    def __init__(self):
        self.mglo = {}
        raise NotImplementedError('SubroutineMap')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = SubroutineMap.__new__(SubroutineMap)
        res.mglo = obj
        return res

    def __getitem__(self, key) -> Subroutine:
        '''
        '''

        return Subroutine.new(self.mglo[key])

    def __contains__(self, key):
        return key in self.mglo

    def __len__(self):
        return len(self.mglo)


class SubroutineUniform:
    '''
        SubroutineUniform
    '''

    def __init__(self):
        self.mglo = None
        raise NotImplementedError('SubroutineUniform')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = SubroutineUniform.__new__(SubroutineUniform)
        res.mglo = obj
        return res

    @property
    def name(self):
        '''
            The name of the subroutine uniform.
        '''

        return self.mglo.name

    @property
    def location(self):
        '''
            The location of the subroutine uniform.
        '''

        return self.mglo.location


class SubroutineUniformMap:
    '''
        SubroutineUniformMap
    '''

    def __init__(self):
        self.mglo = {}
        raise NotImplementedError('SubroutineUniformMap')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = SubroutineUniformMap.__new__(SubroutineUniformMap)
        res.mglo = obj
        return res

    def __getitem__(self, key) -> SubroutineUniform:
        '''
        '''

        return SubroutineUniform.new(self.mglo[key])

    def __contains__(self, key):
        return key in self.mglo

    def __len__(self):
        return len(self.mglo)


class ProgramStage:
    '''
        ProgramStage
    '''

    def __init__(self):
        self.mglo = {}
        raise NotImplementedError('ProgramStage')

    @staticmethod
    def new(obj):
        '''
            For internal use only.
        '''

        res = ProgramStage.__new__(ProgramStage)
        res.mglo = obj
        return res

    @property
    def subroutines(self) -> SubroutineMap:
        '''
            The subroutines of the program_stage.
        '''

        return SubroutineMap.new(self.mglo.subroutines)

    @property
    def subroutine_uniforms(self) -> SubroutineUniformMap:
        '''
            The subroutine_uniforms of the program_stage.
        '''

        return SubroutineUniformMap.new(self.mglo.subroutine_uniforms)
