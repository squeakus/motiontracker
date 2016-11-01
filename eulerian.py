from eularian_magnification.base import eulerian_magnification, show_frequencies
import sys
# show_frequencies('media/face.mp4')

def main(filename):
    eulerian_magnification(filename, image_processing='gaussian', pyramid_levels=3, freq_min=50.0 / 60.0, freq_max=1.0, amplification=50)
    show_frequencies(filename)
    #eulerian_magnification('media/baby.mp4', image_processing='laplacian', pyramid_levels=5, freq_min=0.45, freq_max=1, amplification=50)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Usage %s <videofile>" % sys.argv[0])
        sys.exit(1)

    main(sys.argv[1])
