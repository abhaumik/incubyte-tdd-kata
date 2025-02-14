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

