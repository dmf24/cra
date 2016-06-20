class Sequence:
	"""
	Class to hold information about a single fasta sequence.
	"""
	@staticmethod
	def PLACEHOLDER(length):
		"""
		Variable like structure to act as placeholder of sequences
		"""
		return "X" * length

	def __init__(self, iden, seq):
		self.__identity__ = iden
		self.__sequence__ = seq
		self.__notes__ = None

	def hasSequence(self):
		return len(self.__sequence__)>0 and self.__sequence__[0]!='X'

	def getIdentity(self):
		return self.__identity__

	def getSequence(self):
		return self.__sequence__

	def sequenceLength(self):
		return len(self.__sequence__)

	def getNotes(self):
		return self.__notes__

	def __hash__(self):
		return hash(self.__identity__)

class FastaReader:
	"""
	Class for reading fasta files
	"""
	BADFORMAT = -666
	EOF = False
	__input_file__ = None
	__file_stream__ = None

	def __init__ (self, input_file):
		"""
		Method for initializing fasta reader
		"""
		self.__input_file__ = input_file
		self.__file_stream__ = open(self.__input_file__, "r")

	def __enter__(self):
		assert not self.__file_stream__.closed
		return self

	def readSequence(self):
		"""
		Method for reading a sequence from file
		"""
		identity = self.__file_stream__.readline().rstrip()
		if not identity:
			return EOF
		if identity[0] != '>':
			return self.BADFORMAT
		sequence = self.__file_stream__.readline().rstrip()
		if not sequence:
			return self.BADFORMAT
		return Sequence(identity, sequence)

	def __exit__(self ,type, value, traceback):
		"""
		Method for closing fasta file
		"""
		self.__file_stream__.close()


class FastaWriter:
	"""
	Class for writing to fasta file
	"""

	BADFORMAT = -666
	WRITTENFS = 1

	__output_file__ = None
	__file_stream__ = None


	def __init__(self, output_file, options = "w"):
		"""
		Method for initializing fasta writer with options
		"""
		self.__output_file__ = output_file
		self.__file_stream__ = open(self, options)

	
	def __enter__(self):
		assert not self.__file_stream__.closed
		return self

	def writeSequence(self, sequence):
		"""
		Method for writing sequence into fasta file
		"""
		if sequence.getSequence() is not None and sequence.getIdentity() is not None:
			self.__file_stream__.write(sequence.getIdentity() + " " + sequence.getNotes() + "\n" + sequence.getSequence() + "\n");
			return WRITTENFS
		return BADFORMAT

	def __exit__(self, type, value, traceback):
		"""
		Method for closing fasta file
		"""
		self.__file_stream__.close()