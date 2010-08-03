'''OpenGL extension AMD.name_gen_delete

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_AMD_name_gen_delete'
_DEPRECATED = False
GL_DATA_BUFFER_AMD = constant.Constant( 'GL_DATA_BUFFER_AMD', 0x9151 )
GL_PERFORMANCE_MONITOR_AMD = constant.Constant( 'GL_PERFORMANCE_MONITOR_AMD', 0x9152 )
GL_QUERY_OBJECT_AMD = constant.Constant( 'GL_QUERY_OBJECT_AMD', 0x9153 )
GL_VERTEX_ARRAY_OBJECT_AMD = constant.Constant( 'GL_VERTEX_ARRAY_OBJECT_AMD', 0x9154 )
GL_SAMPLER_OBJECT_AMD = constant.Constant( 'GL_SAMPLER_OBJECT_AMD', 0x9155 )


def glInitNameGenDeleteAMD():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
