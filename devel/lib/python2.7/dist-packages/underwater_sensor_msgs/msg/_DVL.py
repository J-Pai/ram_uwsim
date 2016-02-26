# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from underwater_sensor_msgs/DVL.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class DVL(genpy.Message):
  _md5sum = "c455f331872552e620e26fc7caad335d"
  _type = "underwater_sensor_msgs/DVL"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
string header_dvl
string date 
float64 salinity 
float64 temperature   	# TODO::ARNAU ha de ser generic ?
float64 depth  		# TODO::ARNAU ha de ser generic
float64 sound_speed 
int32 test
#WATER-MASS, INSTRUMENT-REFERENCED VELOCITY DATA
float64 wi_x_axis 
float64 wi_y_axis 
float64 wi_z_axis 
float64 wi_error 
string wi_status 
#BOTTOM-TRACK, INSTRUMENT-REFERENCED VELOCITY DATA
float64 bi_x_axis 
float64 bi_y_axis 
float64 bi_z_axis 
float64 bi_error 
string bi_status 
#WATER-MASS, SHIP-REFERENCED VELOCITY DATA
float64 ws_transverse 
float64 ws_longitudinal 
float64 ws_normal 
string ws_status 
#BOTTOM-TRACK, SHIP-REFERENCED VELOCITY DATA
float64 bs_transverse 
float64 bs_longitudinal 
float64 bs_normal 
string bs_status 
#WATER-MASS, EARTH-REFERENCED VELOCITY DATA
float64 we_east 
float64 we_north 
float64 we_upwards 
string  we_status 
#BOTTOM-TRACK, EARTH-REFERENCED VELOCITY DATA
float64 be_east 
float64 be_north 
float64 be_upwards 
string  be_status 
#  WATER-MASS, EARTH-REFERENCED DISTANCE DATA
float64 wd_east 
float64 wd_north 
float64 wd_upwards 
float64 wd_range 
float64 wd_time 
#BOTTOM-TRACK, EARTH-REFERENCED DISTANCE DATA
float64 bd_east 
float64 bd_north 
float64 bd_upwards 
float64 bd_range 
float64 bd_time
#RAW DATA 
string raw_data

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','header_dvl','date','salinity','temperature','depth','sound_speed','test','wi_x_axis','wi_y_axis','wi_z_axis','wi_error','wi_status','bi_x_axis','bi_y_axis','bi_z_axis','bi_error','bi_status','ws_transverse','ws_longitudinal','ws_normal','ws_status','bs_transverse','bs_longitudinal','bs_normal','bs_status','we_east','we_north','we_upwards','we_status','be_east','be_north','be_upwards','be_status','wd_east','wd_north','wd_upwards','wd_range','wd_time','bd_east','bd_north','bd_upwards','bd_range','bd_time','raw_data']
  _slot_types = ['std_msgs/Header','string','string','float64','float64','float64','float64','int32','float64','float64','float64','float64','string','float64','float64','float64','float64','string','float64','float64','float64','string','float64','float64','float64','string','float64','float64','float64','string','float64','float64','float64','string','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,header_dvl,date,salinity,temperature,depth,sound_speed,test,wi_x_axis,wi_y_axis,wi_z_axis,wi_error,wi_status,bi_x_axis,bi_y_axis,bi_z_axis,bi_error,bi_status,ws_transverse,ws_longitudinal,ws_normal,ws_status,bs_transverse,bs_longitudinal,bs_normal,bs_status,we_east,we_north,we_upwards,we_status,be_east,be_north,be_upwards,be_status,wd_east,wd_north,wd_upwards,wd_range,wd_time,bd_east,bd_north,bd_upwards,bd_range,bd_time,raw_data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DVL, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.header_dvl is None:
        self.header_dvl = ''
      if self.date is None:
        self.date = ''
      if self.salinity is None:
        self.salinity = 0.
      if self.temperature is None:
        self.temperature = 0.
      if self.depth is None:
        self.depth = 0.
      if self.sound_speed is None:
        self.sound_speed = 0.
      if self.test is None:
        self.test = 0
      if self.wi_x_axis is None:
        self.wi_x_axis = 0.
      if self.wi_y_axis is None:
        self.wi_y_axis = 0.
      if self.wi_z_axis is None:
        self.wi_z_axis = 0.
      if self.wi_error is None:
        self.wi_error = 0.
      if self.wi_status is None:
        self.wi_status = ''
      if self.bi_x_axis is None:
        self.bi_x_axis = 0.
      if self.bi_y_axis is None:
        self.bi_y_axis = 0.
      if self.bi_z_axis is None:
        self.bi_z_axis = 0.
      if self.bi_error is None:
        self.bi_error = 0.
      if self.bi_status is None:
        self.bi_status = ''
      if self.ws_transverse is None:
        self.ws_transverse = 0.
      if self.ws_longitudinal is None:
        self.ws_longitudinal = 0.
      if self.ws_normal is None:
        self.ws_normal = 0.
      if self.ws_status is None:
        self.ws_status = ''
      if self.bs_transverse is None:
        self.bs_transverse = 0.
      if self.bs_longitudinal is None:
        self.bs_longitudinal = 0.
      if self.bs_normal is None:
        self.bs_normal = 0.
      if self.bs_status is None:
        self.bs_status = ''
      if self.we_east is None:
        self.we_east = 0.
      if self.we_north is None:
        self.we_north = 0.
      if self.we_upwards is None:
        self.we_upwards = 0.
      if self.we_status is None:
        self.we_status = ''
      if self.be_east is None:
        self.be_east = 0.
      if self.be_north is None:
        self.be_north = 0.
      if self.be_upwards is None:
        self.be_upwards = 0.
      if self.be_status is None:
        self.be_status = ''
      if self.wd_east is None:
        self.wd_east = 0.
      if self.wd_north is None:
        self.wd_north = 0.
      if self.wd_upwards is None:
        self.wd_upwards = 0.
      if self.wd_range is None:
        self.wd_range = 0.
      if self.wd_time is None:
        self.wd_time = 0.
      if self.bd_east is None:
        self.bd_east = 0.
      if self.bd_north is None:
        self.bd_north = 0.
      if self.bd_upwards is None:
        self.bd_upwards = 0.
      if self.bd_range is None:
        self.bd_range = 0.
      if self.bd_time is None:
        self.bd_time = 0.
      if self.raw_data is None:
        self.raw_data = ''
    else:
      self.header = std_msgs.msg.Header()
      self.header_dvl = ''
      self.date = ''
      self.salinity = 0.
      self.temperature = 0.
      self.depth = 0.
      self.sound_speed = 0.
      self.test = 0
      self.wi_x_axis = 0.
      self.wi_y_axis = 0.
      self.wi_z_axis = 0.
      self.wi_error = 0.
      self.wi_status = ''
      self.bi_x_axis = 0.
      self.bi_y_axis = 0.
      self.bi_z_axis = 0.
      self.bi_error = 0.
      self.bi_status = ''
      self.ws_transverse = 0.
      self.ws_longitudinal = 0.
      self.ws_normal = 0.
      self.ws_status = ''
      self.bs_transverse = 0.
      self.bs_longitudinal = 0.
      self.bs_normal = 0.
      self.bs_status = ''
      self.we_east = 0.
      self.we_north = 0.
      self.we_upwards = 0.
      self.we_status = ''
      self.be_east = 0.
      self.be_north = 0.
      self.be_upwards = 0.
      self.be_status = ''
      self.wd_east = 0.
      self.wd_north = 0.
      self.wd_upwards = 0.
      self.wd_range = 0.
      self.wd_time = 0.
      self.bd_east = 0.
      self.bd_north = 0.
      self.bd_upwards = 0.
      self.bd_range = 0.
      self.bd_time = 0.
      self.raw_data = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.header_dvl
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.date
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4di4d.pack(_x.salinity, _x.temperature, _x.depth, _x.sound_speed, _x.test, _x.wi_x_axis, _x.wi_y_axis, _x.wi_z_axis, _x.wi_error))
      _x = self.wi_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4d.pack(_x.bi_x_axis, _x.bi_y_axis, _x.bi_z_axis, _x.bi_error))
      _x = self.bi_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.ws_transverse, _x.ws_longitudinal, _x.ws_normal))
      _x = self.ws_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.bs_transverse, _x.bs_longitudinal, _x.bs_normal))
      _x = self.bs_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.we_east, _x.we_north, _x.we_upwards))
      _x = self.we_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.be_east, _x.be_north, _x.be_upwards))
      _x = self.be_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_10d.pack(_x.wd_east, _x.wd_north, _x.wd_upwards, _x.wd_range, _x.wd_time, _x.bd_east, _x.bd_north, _x.bd_upwards, _x.bd_range, _x.bd_time))
      _x = self.raw_data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header_dvl = str[start:end].decode('utf-8')
      else:
        self.header_dvl = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.date = str[start:end].decode('utf-8')
      else:
        self.date = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.salinity, _x.temperature, _x.depth, _x.sound_speed, _x.test, _x.wi_x_axis, _x.wi_y_axis, _x.wi_z_axis, _x.wi_error,) = _struct_4di4d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.wi_status = str[start:end].decode('utf-8')
      else:
        self.wi_status = str[start:end]
      _x = self
      start = end
      end += 32
      (_x.bi_x_axis, _x.bi_y_axis, _x.bi_z_axis, _x.bi_error,) = _struct_4d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bi_status = str[start:end].decode('utf-8')
      else:
        self.bi_status = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.ws_transverse, _x.ws_longitudinal, _x.ws_normal,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ws_status = str[start:end].decode('utf-8')
      else:
        self.ws_status = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.bs_transverse, _x.bs_longitudinal, _x.bs_normal,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bs_status = str[start:end].decode('utf-8')
      else:
        self.bs_status = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.we_east, _x.we_north, _x.we_upwards,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.we_status = str[start:end].decode('utf-8')
      else:
        self.we_status = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.be_east, _x.be_north, _x.be_upwards,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.be_status = str[start:end].decode('utf-8')
      else:
        self.be_status = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.wd_east, _x.wd_north, _x.wd_upwards, _x.wd_range, _x.wd_time, _x.bd_east, _x.bd_north, _x.bd_upwards, _x.bd_range, _x.bd_time,) = _struct_10d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.raw_data = str[start:end].decode('utf-8')
      else:
        self.raw_data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.header_dvl
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.date
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4di4d.pack(_x.salinity, _x.temperature, _x.depth, _x.sound_speed, _x.test, _x.wi_x_axis, _x.wi_y_axis, _x.wi_z_axis, _x.wi_error))
      _x = self.wi_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4d.pack(_x.bi_x_axis, _x.bi_y_axis, _x.bi_z_axis, _x.bi_error))
      _x = self.bi_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.ws_transverse, _x.ws_longitudinal, _x.ws_normal))
      _x = self.ws_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.bs_transverse, _x.bs_longitudinal, _x.bs_normal))
      _x = self.bs_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.we_east, _x.we_north, _x.we_upwards))
      _x = self.we_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3d.pack(_x.be_east, _x.be_north, _x.be_upwards))
      _x = self.be_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_10d.pack(_x.wd_east, _x.wd_north, _x.wd_upwards, _x.wd_range, _x.wd_time, _x.bd_east, _x.bd_north, _x.bd_upwards, _x.bd_range, _x.bd_time))
      _x = self.raw_data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header_dvl = str[start:end].decode('utf-8')
      else:
        self.header_dvl = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.date = str[start:end].decode('utf-8')
      else:
        self.date = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.salinity, _x.temperature, _x.depth, _x.sound_speed, _x.test, _x.wi_x_axis, _x.wi_y_axis, _x.wi_z_axis, _x.wi_error,) = _struct_4di4d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.wi_status = str[start:end].decode('utf-8')
      else:
        self.wi_status = str[start:end]
      _x = self
      start = end
      end += 32
      (_x.bi_x_axis, _x.bi_y_axis, _x.bi_z_axis, _x.bi_error,) = _struct_4d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bi_status = str[start:end].decode('utf-8')
      else:
        self.bi_status = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.ws_transverse, _x.ws_longitudinal, _x.ws_normal,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ws_status = str[start:end].decode('utf-8')
      else:
        self.ws_status = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.bs_transverse, _x.bs_longitudinal, _x.bs_normal,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.bs_status = str[start:end].decode('utf-8')
      else:
        self.bs_status = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.we_east, _x.we_north, _x.we_upwards,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.we_status = str[start:end].decode('utf-8')
      else:
        self.we_status = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.be_east, _x.be_north, _x.be_upwards,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.be_status = str[start:end].decode('utf-8')
      else:
        self.be_status = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.wd_east, _x.wd_north, _x.wd_upwards, _x.wd_range, _x.wd_time, _x.bd_east, _x.bd_north, _x.bd_upwards, _x.bd_range, _x.bd_time,) = _struct_10d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.raw_data = str[start:end].decode('utf-8')
      else:
        self.raw_data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_4di4d = struct.Struct("<4di4d")
_struct_4d = struct.Struct("<4d")
_struct_10d = struct.Struct("<10d")
_struct_3d = struct.Struct("<3d")
