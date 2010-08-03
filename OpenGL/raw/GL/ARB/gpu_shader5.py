'''OpenGL extension ARB.gpu_shader5

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_gpu_shader5'
_DEPRECATED = False
GL_GEOMETRY_SHADER_INVOCATIONS = constant.Constant( 'GL_GEOMETRY_SHADER_INVOCATIONS', 0x887F )
GL_MAX_GEOMETRY_SHADER_INVOCATIONS = constant.Constant( 'GL_MAX_GEOMETRY_SHADER_INVOCATIONS', 0x8E5A )
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = constant.Constant( 'GL_MIN_FRAGMENT_INTERPOLATION_OFFSET', 0x8E5B )
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = constant.Constant( 'GL_MAX_FRAGMENT_INTERPOLATION_OFFSET', 0x8E5C )
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = constant.Constant( 'GL_FRAGMENT_INTERPOLATION_OFFSET_BITS', 0x8E5D )


def glInitGpuShader5ARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
