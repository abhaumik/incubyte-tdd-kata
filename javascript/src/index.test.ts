import { add } from "./index";

describe("Test add function for simple inputs ", () => {
  it("takes empty input", () => {
    expect(add()).toBe(0);
  });
  it("takes one input", () => {
    expect(add("1")).toBe(1);
  });
  it("takes 2 inputs", () => {
    expect(add("1,5")).toBe(6);
  });
});

describe("Takes any size of string", () => {
  it.each(
    [0, 1, 2, 3, 5, 10, 100].map((numberOfInputs: number) => [
      Array(numberOfInputs).fill(1).toString(),
      numberOfInputs,
    ])
  )('string "%s" with numberOfInputs %i', (str, numberOfInputs) => {
    expect(add(str)).toBe(numberOfInputs);
  });
});

describe("Test for delimiters", () => {
  it("Takes new line as delimiter", () => {
    expect(add("1\n2,3")).toBe(6);
  });
  it("Takes any delimiter", () => {
    expect(add("//;\n1;2")).toBe(3);
  });
});
