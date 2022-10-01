import { RGBColor, HSLColor } from '@/types/color';

export function hexToRGB(hex: string): RGBColor {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex) as RegExpExecArray;

  if (result && result.length !== 4) throw SyntaxError('Incorrect hex color given');

  const r = parseInt(result[1], 16);
  const g = parseInt(result[2], 16);
  const b = parseInt(result[3], 16);

  return {
    r, g, b,
  };
}

export function hexToHSL(hex: string): HSLColor {
  let { r, b, g } = hexToRGB(hex);

  r /= 255;
  g /= 255;
  b /= 255;

  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);

  let h = 0;
  let s = 0;
  const l = (max + min) / 2;

  if (max !== min) {
    const d = max - min;

    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

    switch (max) {
      case r: h = (g - b) / d + (g < b ? 6 : 0); break;
      case g: h = (b - r) / d + 2; break;
      case b: h = (r - g) / d + 4; break;
      default: h = 0; break;
    }

    h /= 6;
  }

  return {
    h,
    s,
    l,
  };
}
